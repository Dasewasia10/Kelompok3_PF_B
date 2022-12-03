from Prototype import varian

maxpro = varian()
maxpro.setNamaVarian("Asus Zenfone Max Pro M1 3/32GB")
maxpro.setRam("3gb")
maxpro.setRom("32gb")
maxpro.setChipset("Snapdragon 636")
maxpro.setBatrai("5000mAh")
print(maxpro.getVarian())

maxpro4 = maxpro.copyVarian()
maxpro4.setNamaVarian("Asus Zenfone Max Pro M1 4/64GB")
maxpro4.setRam("4gb")
maxpro4.setRom("64gb")
print(maxpro4.getVarian())
