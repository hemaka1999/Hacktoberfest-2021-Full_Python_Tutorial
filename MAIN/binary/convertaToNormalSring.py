from struct import unpack
print(unpack('I3c', b'{\x00\x00\x00abc')) # (123, b'a', b'b', b'c')