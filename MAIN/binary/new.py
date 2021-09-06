from struct import pack
print(pack('I3c', 123, b'a', b'b', b'c')) # b'{\x00\x00\x00abc'