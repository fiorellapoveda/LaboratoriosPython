#!/usr/bin/python3

#La función de este código es recibir nombres completos de personas ingresados por un usuario (hasta que este
# indique que quiere SALII). El programa va a procesar los nombres y corregirlos; para cada componente del
# nombre se utilizará la primera letra en mayúscula y las demás en minúscula. Cuando el usuario digite SALIR, se 
# imprimirán todos los nombres que hayan sido ingresados, corregidos. El programa debe verificar que los nombres
# ingresados son correctos (que sólo constan de caracteres y que tienen 3 o 4 componentes.)

#Laboratorio 2 de Python - Fiorella Poveda Chaves (B86145)
#Este laboratorio fue desarrollado con una instalación de Debian 10.9 utilizada a través de WSL 

lista_nombres = []

print('\nBienvenidx!')

while (True):
    nombre_corregido = []
    nombre_ingresado = input('Escriba un nombre completo o SALIR para finalizar el programa: ')

    if ( nombre_ingresado != 'SALIR' ):
        #Se separa el nombre el componentes
        nombre_completo = nombre_ingresado.split(' ')
        #Se verifica la cantidad de componentes
        if ( (len(nombre_completo) > 2) and (len(nombre_completo) <= 4) ):

            #Se verifica que no contenga números 
            if all( x.isalpha() or x.isspace() for x in nombre_ingresado ):

                #Se corrige cada componente según el formato solicitado
                for elemento in nombre_completo:
                    elemento_corregido = elemento.capitalize()
                    nombre_corregido.append(elemento_corregido)
                #Se agrega el nombre corregido a la lista final
                lista_nombres.append(nombre_corregido)
            else:
                print('\nPara que el nombre sea válido, debe contener sólo caracteres.\n')
        else:
            print('\nDebe ingresar un nombre válido.\n')
    else:
        #Se imprime la lista de nombres ingresados cuando el usuario quiera salir
        print('\nNombres ingresados:')
        for elemento in lista_nombres:
            if ( len(elemento) == 3 ):                    
                print(' ' + elemento[0] + ' ' + elemento[1] + ' ' + elemento[2])
            else:
                print(' ' + elemento[0] + ' ' + elemento[1] + ' ' + elemento[2] + ' ' + elemento[3])
        False
        break