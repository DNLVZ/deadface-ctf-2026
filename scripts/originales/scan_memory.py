import mmap,re
with open('memory.raw','rb') as f:
 m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
 for needle in (b'telemetry.ps1','telemetry.ps1'.encode('utf-16le')):
  start=0
  while True:
   p=m.find(needle,start)
   if p<0:break
   b=m[max(0,p-600):p+1000]
   s=b.decode('utf-16le' if b'\0' in needle else 'latin1',errors='replace')
   print(hex(p),re.sub(r'[^\x20-\x7e\r\n\t]','.',s))
   start=p+len(needle)
