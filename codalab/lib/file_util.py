'''
file_util provides helpers for dealing with file handles in robust,
memory-efficent ways.
'''
BUFFER_SIZE = 0x40000

import sys

def copy(source, dest, autoflush=True):
    '''
    Read from the source file handle and write the data to the dest file handle.
    '''
    n = 0
    while True:
        buffer = source.read(BUFFER_SIZE)
        if not buffer:
            break
        dest.write(buffer)
        n += len(buffer)
        print ("\r%s bytes" % n),
        sys.stdout.flush()
        if autoflush:
            dest.flush()
    print ''

def tail(source, num_lines=10):
    return "\n".join(source.read().splitlines()[-10:])
