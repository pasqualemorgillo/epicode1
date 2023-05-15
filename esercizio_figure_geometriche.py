def calcola_perimetro_quadrato():
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    perimetro = lato * 4
    print("Il perimetro del quadrato è di:", perimetro)

def calcola_perimetro_cerchio():
    raggio = float(input("Inserisci il raggio del cerchio: "))
    perimetro = 2 * 3.14 * raggio
    print("Il perimetro del cerchio è di:", perimetro)

def calcola_perimetro_rettangolo():
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro = base * 2 + altezza * 2
    print("Il perimetro del rettangolo è di:", perimetro)

print("Questo è un programma che permette di risolvere il perimetro di 3 figure geometriche")
scelta = input("Scegli tra le seguenti figure geometriche: A) quadrato, B) cerchio, C) rettangolo: ")

if scelta == 'A' or scelta == 'a':
    calcola_perimetro_quadrato()
elif scelta == 'B' or scelta == 'b':
    calcola_perimetro_cerchio()
elif scelta == 'C' or scelta == 'c':
    calcola_perimetro_rettangolo()
else:
    print("Scelta non consentita")

