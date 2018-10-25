#coding:utf-8
import sys

"""
Executable File
"""

if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        rom = bytearray(f.read())
    
    count = 0x10
    program_rom = rom[0x10:0x10 + rom[4] * 0x4000]
    character_rom = rom[0x10 + rom[4] * 0x4000:0x10 + rom[4] * 0x4000 + rom[5] * 0x2000]
    print(len(program_rom))
    print(len(character_rom))
    print(rom[4])

    