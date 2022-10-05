from FrisbeeLuokat import Rata
from FrisbeeLuokat import Pelaaja
from FrisbeeLuokat import Tulos

#-----------------------------------------------------------#

def RataValinnat():
    tempRadat = []
    valinta = 1
    while valinta != 0:
        print("-----------------------")
        valinta = int(input("Valitse 1 syöttääksesi uusi rata, valitse 0 jatkaaksesi"))
        if(valinta == 1):
            rataNumero = int(input("Anna radan numero:"))
            rataPar = int(input("Anna radan PAR lukema:"))
            uusiRata = Rata(rataNumero, rataPar)
            tempRadat.append(uusiRata)
        elif(valinta == 0):
            print("Syötetyt radat:")
            for rata in tempRadat:
                rata.Tulosta()
            print("Jatketaan pelaajan syöttämisellä")
    return tempRadat

def PelaajaValinnat():
    pelaajaValinta = 1
    tempPelaajat = []
    while pelaajaValinta != 0:
        print("-----------------------")
        pelaajaValinta = int(input("Valitse 1 syöttääksesi uuden pelaajan, valitse 0 aloittaaksesi pelin"))
        if(pelaajaValinta == 1):
            pelaajaNimi = input("Syötä pelaajan nimi:")
            pelaajaIka = int(input("Anna pelaajan ikä:"))
            uusiPelaaja = Pelaaja(pelaajaNimi, pelaajaIka)
            tempPelaajat.append(uusiPelaaja)
        elif(pelaajaValinta == 0):
            print("Pelaajat:")
            for peluri in tempPelaajat:
                peluri.Tulosta()
            print("Aloitettaan peli!")
    return tempPelaajat

def Peli(tempRatalista, tempPelaajalista):
    tempTulokset = []
    for rata in tempRatalista:
        print("Rata numero", rata.numero, "Tavoite PAR on", rata.par)
        for pelaaja in tempPelaajalista:
            print("Paljonko henkilö", pelaaja.nimi, "heitti:")
            tulos = int(input())
            uusiTulos = Tulos(pelaaja, rata, tulos)
            tempTulokset.append(uusiTulos)
        print("Siirrytään seuraavalle radalle")
    print("-----------------------")
    print("Peli on loppunut!")
    print("-----------------------")
    return tempTulokset

## Main Code yo 
print("Tervettuloa pelaaman frisbugolffia.")
print("Aloitetaan syöttämällä radat.")
rataLista = RataValinnat()
pelaajaLista = PelaajaValinnat()
tulokset = Peli(rataLista, pelaajaLista)
for pelaaja in pelaajaLista:
    huonoinTulos = 0
    parasTulos = 100
    yhteensa = 0
    for tulos in tulokset:
        if(tulos.pelaaja == pelaaja):
            yhteensa += tulos.tulos
            if(huonoinTulos < tulos.tulos):
                huonoinTulos = tulos.tulos
            if(parasTulos > tulos.tulos):
                parasTulos = tulos.tulos
    keskiarvo = yhteensa/len(rataLista)
    print("-----------------------")
    print(pelaaja.nimi, "Pisteet:", yhteensa, "/KA:", keskiarvo)
    print("Paras tulos:", parasTulos, ", Huonoin heitto:",huonoinTulos)
    print("-----------------------")



           
    
