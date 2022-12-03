class PCGamingGraphic():
    def gamingGraphicCard(self): pass
class PCOfficeGraphic():
    def officeGraphicCard(self): pass

class NvidiaRTX(PCGamingGraphic):
    def gamingGraphicCard(self):
        print("Nvidia Graphic Card dipasangkan ke PC gaming")
class AMDRadeonRX(PCGamingGraphic):
    def gamingGraphicCard(self):
        print("AMD Radeon RX Graphic Card dipasangkan ke PC gaming")
class IntelHD(PCOfficeGraphic):
    def officeGraphicCard(self):
        print("Intel HD Graphic Card dipasangkan ke PC office")

class AMDRadeon(PCOfficeGraphic):
    def officeGraphicCard(self):
        print("AMD Radeon Graphic Card dipasangkan ke PC office")
class PCGraphic:
# disini kita menganalogikan power sebagai besar kekuatan Graphic Card,
# 1 untuk intel HD, 2 untuk AMD Radeon, 3 untuk Nvidia RTX dan 4 untuk AMD
# Radeon RX
    def getGraphic(power): pass
   
class PCGamingGraphic(PCGraphic):
    @staticmethod
    def getGraphic(power):
        if power == 3:
            return NvidiaRTX()
        if power == 4:
            return AMDRadeonRX()
    assert 0, "Graphic Card itu tidak tersedia"

class PCOfficeGraphic(PCGraphic):
    @staticmethod
    def getGraphic(power):
        if power == 1:
            return IntelHD()
        if power == 2:
            return AMDRadeon()
        assert 0, "Graphic Card itu tidak tersedia"


