# python write byte to file

import os

payload  = b'asd\x0aasd\x0a2\x0a1\x0a' + b'%08x'

def write_byte_to_file(file_path, byte):
    with open(file_path, 'wb') as f:
        f.write(byte)
        

def write_byte_to_file_append(file_path, byte):
    with open(file_path, 'ab') as f:
        f.write(byte)

write_byte_to_file('payload', payload)