$source = @'
using System;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections.Generic;
public class MemoryStrings {
 static Regex rx = new Regex(@"\.ps1|schtasks|net use |\\users\\|demonne|de monne|ghosttown|zerotrace", RegexOptions.IgnoreCase|RegexOptions.Compiled);
 static HashSet<string> seen = new HashSet<string>();
 static void Emit(StringBuilder s, StreamWriter w) { if(s.Length>=7) { string t=s.ToString(); if(rx.IsMatch(t)&&seen.Add(t)) w.WriteLine(t); } s.Clear(); }
 public static void Scan(string file,string output) {
  using(var f=new FileStream(file,FileMode.Open,FileAccess.Read,FileShare.ReadWrite)) using(var w=new StreamWriter(output,false,Encoding.UTF8)) {
   byte[] b=new byte[8*1024*1024]; var a=new StringBuilder();var u=new StringBuilder();var v=new StringBuilder(); int last=0;long pos=0; int n;
   while(pos<8589934592L) { n=f.Read(b,0,b.Length); if(n==0){System.Threading.Thread.Sleep(1000);continue;} for(int i=0;i<n;i++,pos++) {int c=b[i];
    if(c>=32&&c<=126) {a.Append((char)c);if(a.Length>=8192)Emit(a,w);}else Emit(a,w);
    if((pos&1)==1) {if(c==0&&last>=32&&last<=126){u.Append((char)last);if(u.Length>=8192)Emit(u,w);}else Emit(u,w);}
    else if(pos>0) {if(c==0&&last>=32&&last<=126){v.Append((char)last);if(v.Length>=8192)Emit(v,w);}else Emit(v,w);}
    last=c;
   } w.Flush(); }
   Emit(a,w);Emit(u,w);Emit(v,w);
  }
 }
}
'@
Add-Type -TypeDefinition $source
[MemoryStrings]::Scan((Join-Path $PWD 'memory.raw'), (Join-Path $PWD 'memory-hits.txt'))
Get-Content memory-hits.txt | Select-Object -First 100
