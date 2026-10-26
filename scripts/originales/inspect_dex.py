import struct,pathlib
b=pathlib.Path('apk-expanded/classes.dex').read_bytes()
u32=lambda p:struct.unpack_from('<I',b,p)[0]
u16=lambda p:struct.unpack_from('<H',b,p)[0]
def leb(p):
 v=0;s=0
 while True:
  c=b[p];p+=1;v|=(c&127)<<s;s+=7
  if c<128:return v,p
ss=[]
for i in range(u32(56)):
 p=u32(u32(60)+4*i);_,p=leb(p);e=b.index(0,p);ss.append(b[p:e].decode('utf8','replace'))
ts=[ss[u32(u32(68)+4*i)] for i in range(u32(64))]
for i in range(u32(96)):
 o=u32(100)+32*i;cl=ts[u32(o)]
 if not cl.startswith('Lcom/demonne/'):continue
 p=u32(o+24)
 if not p:continue
 counts=[]
 for _ in range(4):v,p=leb(p);counts.append(v)
 for _ in range(sum(counts[:2])):_,p=leb(p);_,p=leb(p)
 for count in counts[2:]:
  idx=0
  for _ in range(count):
   d,p=leb(p);idx+=d;_,p=leb(p);code,p=leb(p)
   if not code:continue
   name=ss[u32(u32(92)+8*idx+4)];size=u32(code+12);found=[]
   for k in range(size):
    q=code+16+2*k;op=b[q]
    if op==26 and k+1<size:
     j=u16(q+2)
     if j<len(ss):found.append(ss[j])
    if op==27 and k+2<size:
     j=u32(q+2)
     if j<len(ss):found.append(ss[j])
   if found:print(cl,name,repr(found))
   if cl=='Lcom/demonne/financial/LoginActivity;' and name in ('performInternalLogin','attemptLogin'):
    for k in range(size):
     q=code+16+2*k;op=b[q];extra=''
     if op in (0x6e,0x6f,0x70,0x71,0x72,0x74,0x75,0x76,0x77,0x78) and k+1<size:
      mi=u16(q+2)
      if mi<u32(88):
       mo=u32(92)+8*mi;extra=ts[u16(mo)]+' '+ss[u32(mo+4)]
     print(f'{k:04x}: {u16(q):04x} {extra}')
