$src = @'
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
public class CaptureReview {
static int U16(byte[] b,int p){return (b[p]<<8)|b[p+1];}
public static void Run(string path,string folder){
Directory.CreateDirectory(folder);var b=File.ReadAllBytes(path);Console.WriteLine(BitConverter.ToString(b,0,24));
var counts=new Dictionary<string,int>();var streams=new Dictionary<string,MemoryStream>();int num=0;
for(int p=24;p+16<=b.Length;){int n=BitConverter.ToInt32(b,p+8);int start=p+16,end=start+n;if(n<14||end>b.Length)break;num++;int ip=start+14;int et=U16(b,start+12);if(et==0x8100){ip+=4;et=U16(b,start+16);}if(et==0x0800&&ip+20<end){int proto=b[ip+9],tr=ip+(b[ip]&15)*4;string from=new System.Net.IPAddress(new byte[]{b[ip+12],b[ip+13],b[ip+14],b[ip+15]}).ToString(),to=new System.Net.IPAddress(new byte[]{b[ip+16],b[ip+17],b[ip+18],b[ip+19]}).ToString();int sp=0,dp=0,data=tr;if((proto==6||proto==17)&&tr+8<=end){sp=U16(b,tr);dp=U16(b,tr+2);data=proto==6?tr+((b[tr+12]>>4)*4):tr+8;}string key=proto+"_"+from+"_"+sp+"_to_"+to+"_"+dp;if(!counts.ContainsKey(key))counts[key]=0;counts[key]++;if(data<end&&(proto==6||proto==17)){if(!streams.ContainsKey(key))streams[key]=new MemoryStream();streams[key].Write(b,data,end-data);}}
p=end;}
Console.WriteLine("PACKETS "+num);foreach(var kv in counts)Console.WriteLine(kv.Value+" "+kv.Key);foreach(var kv in streams)File.WriteAllBytes(Path.Combine(folder,kv.Key+".bin"),kv.Value.ToArray());
}}
'@
Add-Type -TypeDefinition $src
[CaptureReview]::Run((Join-Path $PWD 'DontLeaveMeHanging.pcap'),(Join-Path $PWD 'hanging_flows'))
