#!/usr/bin/python3

iterador = int(input('Ingrese el interador para la pirámide: '))
caracter = str(input('Ingrese el caracter para imprimir la piramide: '))

for a in range(iterador):
    for b in range(iterador):
        if b <= a:
            print(caracter, end = "")
        if b == a:
            print("")
