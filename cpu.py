#coding:utf-8

"""
CPU6502
"""

class Cpu:
    def __init__(self, program_rom):
        self.memory = bytearray(b'0' * 0x10000)
        self.registerA = 0 
        self.registerX = 0
        self.registerY = 0
        self.registerS = 0
        self.program_counter = 0x8000

    def immediate(self):
        address = self.program_counter + 1
        self.program_counter += 2
        return address
    
    def zeropage(self):
        address = self.program_counter + 1
        self.program_counter += 2
        return self.memory[address]

    def zeropage_x(self):
        address = self.program_counter + 1
        self.program_counter += 2
        return (self.memory[address] + registerX) & 0xff

    def zeropage_y(self):
        address = self.program_counter + 1
        self.program_counter += 2
        return (self.memory[address] + registerY) & 0xff

    def absolute(self):
        address = (self.memory[self.program_counter + 2] * 0x100 + self.memory[self.program_counter + 1]) & 0xffff
        self.program_counter += 3
        return address
    
    def absolute_x(self):
        address = (self.memory[self.program_counter + 2] * 0x100 + self.memory[self.program_counter + 1]) & 0xffff
        self.program_counter += 3
        return (address + self.registerX) & 0xffff

    def absolute_y(self):
        address = (self.memory[self.program_counter + 2] * 0x100 + self.memory[self.program_counter + 1]) & 0xffff
        self.program_counter += 3
        return (address + self.registerY) & 0xffff