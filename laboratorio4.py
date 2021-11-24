#!/usr/bin/python3

#Laboratorio 4 de Python - Fiorella Poveda Chaves (B86145)
#Este laboratorio fue desarrollado con una instalación de Debian 10.9 utilizada a través de WSL 
"""
En el presente código se trabaja con una clase para representar matrices. Dicha clase cuenta con distintas funciones que permiten
realizar distintas operaciones entre dos matrices. Además de las funciones, se tomó en cuenta el manejo de errores.
"""
#Cambiar valores de las matrices

class Matriz:
    """
    Clase para representar matrices n x m: n = filas, m = columnas
    """
    #Método constructor
    def __init__(self, filas, columnas):
        self.filas = int(filas)
        self.columnas = int(columnas)
        self.matriz = [[0] * self.columnas for n in range(self.filas)]

    #Método para representar la matriz como un string
    def __str__(self):
        filas_en_string = [ ' '.join([str(self.matriz[fila][columna]) 
            for columna in range(self.columnas)]) 
            for fila in range(self.filas)]
        return '\n'.join(filas_en_string)

    #Método para obtener el elemento en alguna coordenada dada
    def get(self, fila, columna):
        if ( (type(fila) != int) or (type(columna) != int) ):
            raise TypeError  
        if ( (fila not in range(self.filas)) or (columna not in range(self.columnas)) ):
            raise Exception('ERROR, las coordenadas {},{} no son válidas.'.format(fila,columna))
        return self.matriz[fila][columna]

    #Método para asignar un valor a un elemento dado por una coordenada
    def set(self, fila, columna, nuevo_valor):
        if ( (type(fila) != int) or (type(columna) != int) or (type(nuevo_valor) != (int or float))):
            raise TypeError  
        if ( (fila not in range(self.filas)) or (columna not in range(self.columnas)) ):
            raise Exception('ERROR, las coordenadas {},{} no son válidas.'.format(fila,columna))
        self.matriz[fila][columna] = nuevo_valor

    #Método para sumar dos matrices
    def __add__(self, other):
        if ( (self.filas != other.filas) or (self.columnas != other.columnas) ):
            raise Exception ('Las matrices no pueden sumarse porque son de diferente tamaño.')
        resultado_suma = Matriz(self.filas, self.columnas)
        for n in range(self.filas):
            for m in range(self.columnas):
                resultado_suma.matriz[n][m] = self.matriz[n][m] + other.matriz[n][m]
        return resultado_suma

    #Método para restar dos matrices
    def __sub__(self, other):
        if ( (self.filas != other.filas) or (self.columnas != other.columnas) ):
            raise Exception ('Las matrices no pueden restarse porque son de diferente tamaño.')
        resultado_resta = Matriz(self.filas, self.columnas)
        for n in range(self.filas):
            for m in range(self.columnas):
                resultado_resta.matriz[n][m] = self.matriz[n][m] - other.matriz[n][m]
        return resultado_resta

    def __getitem__(self, fila):
        if ( fila not in range(self.filas) ):
            raise Exception('La fila {} es invalida.'.format(fila))
        return self.matriz[fila]

    #Método para multiplicar dos matricces
    def __matmul__(self, other):
        if ( isinstance(other,Matriz) ):
            resultado_mult = Matriz(self.filas,self.columnas)
            #Se multiplican los elementos en la misma fila de la primer matriz con los elementos en la misma columna de la segunda matriz
            for n in range(self.filas):
                for m in range(self.columnas):
                    acc = 0
                    for l in range(self.filas):
                        acc += self.matriz[n][l] * other.matriz[l][m]
                        resultado_mult.matriz[n][m] = acc
        return resultado_mult

    #Método para obtener la transpuesta de una matriz
    def transpose(self):
        self.filas, self.columnas = self.columnas, self.filas
        self.matriz = [list(item) for item in zip(*self.matriz)]

    #Método que va a retornar la transpuesta de una matriz dada sin modificar esta última
    def getTranspose(self):
        filas, columnas = self.columnas, self.filas
        transpuesta = Matriz(filas, columnas)
        transpuesta.matriz =  [list(item) for item in zip(*self.matriz)]
        return transpuesta

#Programa de ejemplo para mostrar la funcionalidad de las funciones definidas anteriormente
if __name__ == '__main__':
    matriz_1 = Matriz(4,4)
    print('Matriz 1: {}'.format(matriz_1.matriz))
    print('Matriz 1 impresa de manera diferente:')
    print(matriz_1)
    valor = matriz_1.get(3,2)
    print('El valor en la coordenada (3,2) en la matriz 1 es: {}'.format(valor))
    nuevo_valor1 = matriz_1.set(3,2,5)
    nuevo_valor2 = matriz_1.set(3,3,7)
    nuevo_valor3 = matriz_1.set(0,1,3)
    nuevo_valor4 = matriz_1.set(1,1,4)
    print('Se realizaron cambios en algunos valores de la matriz...\nLa nueva matriz es: ')
    print(matriz_1)

    matriz_2 = Matriz(4,4)
    matriz_2.set(0,0,9)
    matriz_2.set(2,2,6)
    matriz_2.set(1,0,5)
    matriz_2.set(3,2,7)
    print('Matriz 2:')
    print(matriz_2)

    print('Suma:')
    print(matriz_1 + matriz_2)
    print('Resta:')
    print(matriz_1 - matriz_2)
    print('Multiplicación:')
    print(matriz_1 @ matriz_2)
    matriz_2.transpose()
    print('Matriz 2 transpuesta:')
    print(matriz_2)
    print('Obteniendo fila 2 de la matriz 2...')
    print(matriz_2[2])
    print('Obteniendo coordenada 3, 1 de la matriz 2...')
    print(matriz_2[2][3])