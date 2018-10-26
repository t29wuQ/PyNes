#coding:utf-8

"""
CPU6502
"""

class Cpu:
    def __init__(self, program_rom):
        self.memory = bytearray(b'0' * 0x8000)
        self.registerA = 0 
        self.registerX = 0
        self.registerY = 0
        self.registerS = 0xff
        self.memory += program_rom
        self.n_flag = 0
        self.v_flag = 0
        self.b_flag = 0
        self.i_flag = 0
        self.z_flag = 0
        self.c_flag = 0

    def test(self, value):
        self.memory[2] = value
        print(self.memory[2])


    def fetch_memory(self, address):
        return self.memory[address]

    def write_memory(self, address, value):
        self.memory[address] = value

    def check_flag_n_z(self, value):
        if self.z_flag == 0:
            self.z_flag = 1
        else:
            self.z_flag = 0
        self.n_flag

    """
    アドレッシングここから
    """

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

    """
    アドレッシングここまで
    """



    """
    命令セットここから
    """

    def lda(self, address):
        self.registerA = self.FetchMemory(adderess) & 0xff
        self.check_flag_n_z(self.registerA)

    def ldx(self, address):
        self.registerX= self.FetchMemory(adderess) & 0xff
        self.check_flag_n_z(self.registerX)

    def ldy(self, address):
        self.registerY = self.FetchMemory(adderess) & 0xff
        self.check_flag_n_z(self.registerY)

    
    def adc(self, address):
        sum = self.registerA + self.fetch_memory(address) + self.c_flag
        self.registerA = sum & 0xff
        self.check_flag_n_z(self.registerA)
        self.v_flag = 
        if sum > 0xff:
            self.c_flag = 1
        else:
            self.c_flag = 0
        


    """
    命令セットここまで
    """