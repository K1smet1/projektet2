class Libraria:
    def __init__(self):
        self.inventar = []

    def shto_liber(self, titull, autor, isbn):
        self.inventar.append({"Titull": titull, "Autor": autor, "ISBN": isbn})
        print(f"Libri '{titull}' u shtua me sukses!\n")

    def kerko_liber(self, fjale_celes):
        rezultate = [liber for liber in self.inventar if fjale_celes.lower() in liber["Titull"].lower() or fjale_celes.lower() in liber["Autor"].lower()]
        if rezultate:
            print("Librat e gjetur:")
            for liber in rezultate:
                print(f"Titull: {liber['Titull']}, Autor: {liber['Autor']}, ISBN: {liber['ISBN']}")
        else:
            print("Nuk u gjet asnjë libër me këtë fjalë kyçe.\n")

    def shfaq_inventarin(self):
        if not self.inventar:
            print("Nuk ka libra në inventar.\n")
        else:
            print("Inventari i librave:")
            for liber in self.inventar:
                print(f"Titull: {liber['Titull']}, Autor: {liber['Autor']}, ISBN: {liber['ISBN']}")

if __name__ == "__main__":
    libraria = Libraria()
    while True:
        print("\nZgjidhni një funksion:")
        print("1. Shto libër")
        print("2. Kërko libër")
        print("3. Shfaq inventarin")
        print("4. Dalje")
        
        zgjedhja = input("Zgjedhni një opsion (1-4): ")
        
        if zgjedhja == "1":
            titull = input("Shkruani titullin e librit: ")
            autor = input("Shkruani autorin e librit: ")
            isbn = input("Shkruani ISBN e librit: ")
            libraria.shto_liber(titull, autor, isbn)
        
        elif zgjedhja == "2":
            fjale_celes = input("Shkruani një fjalë kyçe për kërkimin: ")
            libraria.kerko_liber(fjale_celes)
        
        elif zgjedhja == "3":
            libraria.shfaq_inventarin()
        
        elif zgjedhja == "4":
            print("Dalje nga programi.")
            break
        
        else:
            print("Zgjedhje e pavlefshme, provoni përsëri.")
