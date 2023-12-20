def elsofeladat():
    i: int = 0
    het_napja = input("Kérem adja meg a hét napját: ")
    ora_neve = input("Adja meg az óra nevét: ")
    ertekeles = int(input("Kérem adja meg az értékelést (0-5): "))

    while  not (ertekeles <=5  and ertekeles >= 0):
        ertekeles = int(input("Kérem adja meg az értékelést (0-5): "))
        if ertekeles < 0:
            print("Az értékelés nem lehet negatív!")
        elif ertekeles > 5:
            print("5 pont feletti értékelés nem elfogadható!")
        i +=1

    print(f"I/A,B:\t\n Hét napja: {het_napja}\n Óra neve: {ora_neve}\n Értékelés (0-5): {ertekeles}")
    
    print(f"I/C:\t\n Köszönjük az értékelést!\n Összefoglaló: '{het_napja}', '{ora_neve}', {ertekeles} érték")

