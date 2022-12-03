class Mencuci:
    def cuci(self):
        print("Mencuci...")
 
 
class Membilas:
    def bilas(self):
        print("Membilas...")
 
 
class Memutar:
    def putar(self):
        print("Memutar...")
 
 
class WashingMachine:
    '''Facade'''
 
    def __init__(self):
        self.mencuci = Mencuci()
        self.membilas = Membilas()
        self.memutar = Memutar()
 
    def mulaiMencuci(self):
        self.mencuci.cuci()
        self.membilas.bilas()
        self.memutar.putar()
 
""" main method """
if __name__ == "__main__":
 
    washingMachine = WashingMachine()
    washingMachine.mulaiMencuci()