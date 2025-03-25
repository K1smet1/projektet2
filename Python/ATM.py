class Bankomat:
    def __init__(self, bilanc=0):
        self.bilanc = bilanc

    def shiko_bilancin(self):
        print(f"Bilanci juaj është: ${self.bilanc:.2f}")

    def depozito(self, shume):
        if shume > 0:
            self.bilanc += shume
            print(f"Keni depozituar ${shume:.2f}. Bilanci i ri: ${self.bilanc:.2f}")
        else:
            print("Shuma e depozitës është e pavlefshme.")

    def terheq(self, shume):
        if 0 < shume <= self.bilanc:
            self.bilanc -= shume
            print(f"Keni tërhequr ${shume:.2f}. Bilanci i mbetur: ${self.bilanc:.2f}")
        else:
            print("Shuma e tërheqjes është e pavlefshme ose nuk keni fonde të mjaftueshme.")


def kryesore():
    bankomat = Bankomat(bilanc=10000) 
    
    while True:
        print("\nMenyja e Bankomatit:")
        print("1. Shiko Bilancin")
        print("2. Depozito Para")
        print("3. Tërheq Para")
        print("4. Dil")
        
        zgjedhja = input("Zgjidhni një opsion: ")
        
        if zgjedhja == "1":
            bankomat.shiko_bilancin()
        elif zgjedhja == "2":
            shume = float(input("Shkruani shumën për depozitë: "))
            bankomat.depozito(shume)
        elif zgjedhja == "3":
            shume = float(input("Shkruani shumën për tërheqje: "))
            bankomat.terheq(shume)
        elif zgjedhja == "4":
            print("Faleminderit që përdorët bankomatin. Mirupafshim!")
            break
        else:
            print("Zgjedhje e pavlefshme. Ju lutemi provoni përsëri.")


if __name__ == "__main__":
    kryesore()