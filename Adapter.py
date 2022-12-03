class SepedaMotor:
    def __init__(self):
        self.name = "Sepeda Motor"
 
    def RodaDua(self):
        return "Roda Dua"
 
class Truk:
    def __init__(self):
        self.name = "Truk"
 
    def RodaDelapan(self):
        return "Roda Delapan"
 
class Mobil:
    def __init__(self):
        self.name = "Mobil"
 
    def RodaEmpat(self):
        return "Roda Empat"


class Adapter:
    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)
 
    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)
 
    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__
 
 
""" main method """
if __name__ == "__main__":
 
    """list to store objects"""
    objects = []
 
    sepedaMotor = SepedaMotor()
    objects.append(Adapter(sepedaMotor, wheels = sepedaMotor.RodaDua))
 
    truk = Truk()
    objects.append(Adapter(truk, wheels = truk.RodaDelapan))
 
    mobil = Mobil()
    objects.append(Adapter(mobil, wheels = mobil.RodaEmpat))
 
    for obj in objects:
       print("{0} adalah kendaraan bertipe {1}".format(obj.name, obj.wheels()))