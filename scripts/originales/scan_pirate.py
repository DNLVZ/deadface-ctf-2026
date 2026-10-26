import pathlib, re, struct, collections
p=pathlib.Path('pirate-work/pirateslife.pcap')
hosts=collections.Counter(); agents=collections.Counter(); ips=collections.Counter(); ports=collections.Counter(); dns=collections.Counter()
with p.open('rb') as f:
 h=f.read(4); ng=h==b'\x0a\x0d\x0d\x0a';f.seek(0);endian='<';link=1
 if not ng:
  h=f.read(24);endian='<' if h[:4] in (b'\xd4\xc3\xb2\xa1',b'\x4d\x3c\xb2\xa1') else '>';link=struct.unpack(endian+'I',h[20:24])[0]
 n=0
 while True:
  if ng:
   h=f.read(8)
   if len(h)<8:break
   typ,size=struct.unpack('<II',h);block=f.read(size-8)
   if typ!=6:continue
   cap=struct.unpack('<I',block[12:16])[0];b=block[20:20+cap]
  else:
   h=f.read(16)
   if len(h)<16: break
   sec,usec,cap,orig=struct.unpack(endian+'IIII',h); b=f.read(cap)
  n+=1
  if b'HTTP/' in b or b'GET /' in b or b'POST /' in b:print('HTTP',n,repr(b[-min(len(b),3500):]),flush=True)
  for m in re.findall(rb'deadface\{[^}\r\n]{1,250}\}',b):print('FLAG',n,m,flush=True)
  for m in re.findall(rb'Host: ([^\r\n]+)',b):hosts[m.decode(errors='replace')]+=1
  for m in re.findall(rb'User-Agent: ([^\r\n]+)',b):agents[m.decode(errors='replace')]+=1
  off=14 if link==1 else 0
  if len(b)>off+40 and b[off]>>4==4:
   ip=b[off:]; ihl=(ip[0]&15)*4; src='.'.join(map(str,ip[12:16]));dst='.'.join(map(str,ip[16:20]));ips[(src,dst)]+=1
   if ip[9] in (6,17):
    sp,dp=struct.unpack('!HH',ip[ihl:ihl+4]); ports[(ip[9],dp)]+=1
    if ip[9]==17 and dp==53:
     q=ip[ihl+20:]; parts=[];z=0
     try:
      while q[z]:l=q[z];parts.append(q[z+1:z+1+l].decode(errors='replace'));z+=l+1
      dns['.'.join(parts)]+=1
     except (IndexError,ValueError):pass
print('PACKETS',n,'HOSTS',hosts,'AGENTS',agents,'IPS',ips.most_common(25),'PORTS',ports.most_common(25),'DNS',dns,sep='\n')
