#!/usr/bin/python3

#Laboratorio 3 de Python - Fiorella Poveda Chaves (B86145)
#Este laboratorio fue desarrollado con una instalación de Debian 10.9 utilizada a través de WSL 
"""
El presente código, luego de recibir parámetros ingresados a través de la consola al ejecutar el .py,
realizará un cálculo de la serie de fibonacci para el índice que sea ingresado por el usuario. Además de esto,
en caso de que se ingresen ciertos parámetros opcionales, se imprimirán otras cosas:

:param args.posicion: indice de la serie para el que se hará el cálculo de fibonacci.
:param args.tiempo: si es ingresado, se imprimirá el tiempo total de ejecución del programa.
:param args.completa: si es ingresado, se imprimirá la serie de fibonacci completa hasta el indice indicado.
"""

import argparse
import time

def fibonacci_completa(numero):
    indice_0, indice_1 = 1, 1
    suma, contador = 0, 1
    print('La serie de Fibonacci hasta el índice {} es: '.format(numero))
    while (contador <= numero):
        print(suma)
        contador += 1
        indice_0 = indice_1
        indice_1 = suma
        suma = indice_0 + indice_1

def fibonacci_sencilla(numero):
    if ( (numero == 0) or (numero == 1) ):
        return 1
    else:
      return (fibonacci_sencilla( numero-1 ) + fibonacci_sencilla( numero-2))

def main():
    #Definición de los argumentos para que puedan ser ingresados por consola
    parser = argparse.ArgumentParser()
    parser.add_argument('posicion', 
        help='Posicion en la secuencia de Fibonacci que debe ser calculado.',
        type=int,
    )
    parser.add_argument('--tiempo','-t',
        action='store_true',
        help='Imprime el tiempo transcurrido para finalizar el cálculo.'
    )
    parser.add_argument('--completa','-c',
        action='store_true',
        help='Imprime la secuencia completa.'
    )
    args = parser.parse_args()
    
    #Se llama a la función fibonacci_sencilla
    resultado = fibonacci_sencilla(args.posicion)
    print('El número de fibonacci en el índice ' + str(args.posicion) + ' es: ' + str(resultado))
    
    #Si existe el argumento opcional args.tiempo se ejecuta el siguiente bloque de código
    if args.tiempo:
        inicio = time.time()
        final = time.time()
        tiempo = final - inicio
        print('El tiempo total de ejecución es: ' + str(tiempo) + ' segundos.')
    
    #Si existe el argumento opcional args.completa se ejecuta el siguiente bloque de código que llama a la función fibonacci completa.
    if args.completa:
        lista_fibonacci = fibonacci_completa(args.posicion)

#Se llama a la función main para que se ejecute el programa.
if __name__ == '__main__':
    main()