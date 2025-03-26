def veprime_aritmetike(a, b):
    try:
        return {
            'shuma': a + b,
            'diferenca': a - b,
            'prodhimi': a * b,
            'pjesetimi': a / b if b != 0 else 'e papërcaktuar'
        }
    except Exception as e:
        return {'gabim': str(e)}

def statistika_bazë(te_dhena):
    try:
        te_dhena.sort()
        n = len(te_dhena)
        mesatarja = sum(te_dhena) / n
        mediana = te_dhena[n // 2] if n % 2 == 1 else (te_dhena[n // 2 - 1] + te_dhena[n // 2]) / 2
        varianca = sum((x - mesatarja) ** 2 for x in te_dhena) / n
        devijimi_standard = varianca ** 0.5
        return {
            'mesatarja': mesatarja,
            'mediana': mediana,
            'devijimi_standard': devijimi_standard,
            'varianca': varianca
        }
    except Exception as e:
        return {'gabim': str(e)}

def manipulim_te_dhenash(te_dhena):
    try:
        kolona_statistika = {}
        for kolon, vlera in te_dhena.items():
            kolona_statistika[kolon] = statistika_bazë(vlera)
        return kolona_statistika
    except Exception as e:
        return f"Gabim gjatë përpunimit të të dhënave: {e}"

if __name__ == "__main__":
    while True:
        print("\nZgjidhni një funksion:")
        print("1. Veprime Aritmetike")
        print("2. Statistika Bazë")
        print("3. Manipulim të Dhënash")
        print("4. Dalje")
        
        zgjedhja = input("Zgjedhni një opsion (1-4): ")
        
        if zgjedhja == "1":
            a = float(input("Shkruani numrin e parë: "))
            b = float(input("Shkruani numrin e dytë: "))
            print("Rezultati:", veprime_aritmetike(a, b))
        
        elif zgjedhja == "2":
            te_dhena = list(map(float, input("Shkruani numrat e ndarë me hapësirë: ").split()))
            print("Statistikat:", statistika_bazë(te_dhena))
        
        elif zgjedhja == "3":
            rreshta = int(input("Sa rreshta të dhënash dëshironi të fusni? "))
            te_dhena = {}
            for _ in range(rreshta):
                kolonat = input("Shkruani emrin e kolonës dhe vlerat e ndara me hapësirë (p.sh. A 1 2 3 4): ").split()
                te_dhena[kolonat[0]] = list(map(float, kolonat[1:]))
            print("Manipulim të Dhënash:")
            print(manipulim_te_dhenash(te_dhena))
        
        elif zgjedhja == "4":
            print("Dalje nga programi.")
            break
        
        else:
            print("Zgjedhje e pavlefshme, provoni përsëri.")