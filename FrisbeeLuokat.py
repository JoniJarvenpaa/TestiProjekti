class Rata:
    numero = 0
    par = 0

    def __init__(self, n, p):
        self.numero = n
        self.par = p

    def Tulosta(self):
        print("Rata:", self.numero, "- PAR:",self.par)

class Pelaaja:
    nimi = ""
    ika = 0

    def __init__(self, n, i):
        self.nimi = n
        self.ika = i

    def Tulosta(self):
        print("Nimi:", self.nimi, ", Ikä:", self.ika)

class Tulos:
    pelaaja = Pelaaja("", 0)
    rata = Rata(0,0)
    tulos = 0

    def __init__(self, p, r, t):
        self.pelaaja = p
        self.rata = r
        self.tulos = t