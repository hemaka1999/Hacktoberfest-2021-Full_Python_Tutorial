import struct
import sys

print("Native byteorder: ", sys.byteorder)
# If no byteorder is specified, native byteorder is used
buffer = struct.pack("ihb", 3, 4, 5)
print("Byte chunk: ", repr(buffer))
print("Byte chunk unpacked: ", struct.unpack("ihb", buffer))
# Last element as unsigned short instead of unsigned char ( 2 Bytes)
buffer = struct.pack("ihh", 3, 4, 5)
print("Byte chunk: ", repr(buffer))