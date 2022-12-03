class varian(object):
    name = None
    ram = None
    rom = None
    chipset = None
    batrai = None

    def setNamaVarian(self, name):
        self.name = name
        return self

    def setRam(self, ram):
        self.ram = ram
        return self

    def setRom(self, rom):
        self.rom = rom
        return self

    def setChipset(self, chipset):
        self.chipset = chipset
        return self

    def setBatrai(self, batrai):
        self.batrai = batrai
        return self

    def getVarian(self):
        msg = "Varian dibuat\n"
        msg += f"name = {self.name}\n"
        msg += f"ram = {self.ram}\n"
        msg += f"rom = {self.rom}\n"
        msg += f"chipset = {self.chipset}\n"
        msg += f"batrai = {self.batrai}\n"
        return msg

    def copyVarian(self):
        return varian()\
        .setNamaVarian(self.name)\
        .setRam(self.ram)\
        .setRom(self.rom)\
        .setChipset(self.chipset)\
        .setBatrai(self.batrai)

