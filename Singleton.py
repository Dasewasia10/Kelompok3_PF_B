class kategori():
    # Instance
    __instance = None

    def __new__(cls, deskripsi = None):
        if kategori.__instance == None:
            kategori.__instance = object.__new__(cls)
        kategori.__instance.deskripsi = deskripsi
        return kategori.__instance
