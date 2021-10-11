from os import utime
from sys import version
import urllib.request
import urllib.parse
import http.client
import json

def Verificar(entrada):
    while True: 
        try:
            salida=int(input(entrada))
        except ValueError:
            print("Reintente ingresar numeros")
            continue
        else:
            return salida
            break

try:
    while True:
        print('Operaciones Básicas')
        print('1. Suma\n')
        print('2. Resta\n')
        print('3. Multiplicacion\n')
        print('4. Division\n')
        print('5. Salir')

        while True: 
            opcion = Verificar("Ingrese una opcion: ")
            if opcion in [1,2,3,4,5]: 
                break
            print("Ingrese una opcion valida")

        if opcion == 1: 
            x=Verificar("\n Ingrese primer valor: ")
            y=Verificar("\n Ingrese segundo valor: ")
            url="http://127.0.0.1:8080/suma/{}/{}".format(x,y)
            f = urllib.request.urlopen(url, timeout=30)
            djson = json.loads(f.read())
            print('')
            print(djson)
            print('')
        
        if opcion == 2: 
            x=Verificar("\n Ingresar primer valor: ")
            y=Verificar("\n Ingrese segundo valor: ")
            url ="http://127.0.0.1:8080/resta/{}/{}".format(x,y)
            f= urllib.request.urlopen(url, timeout=30)
            djson = json.loads(f.read())
            print('')
            print(djson)
            print('')
        
        if opcion == 3: 
            x=Verificar("\n Ingresar primer valor: ")
            y=Verificar("\n Ingrese segundo valor: ")
            url ="http://127.0.0.1:8080/multiplicacion/{}/{}".format(x,y)
            f= urllib.request.urlopen(url, timeout=30)
            djson = json.loads(f.read())
            print('')
            print(djson)
            print('')

        if opcion == 4: 
            x=Verificar("\n Ingresar primer valor: ")
            y=Verificar("\n Ingrese segundo valor: ")
            url ="http://127.0.0.1:8080/division/{}/{}".format(x,y)
            f= urllib.request.urlopen(url, timeout=30)
            djson = json.loads(f.read())
            print('')
            print(djson)
            print('')

        if opcion == 5: 
            print("***** ADIOS *****")
            break

except ValueError:
    print("Error al conectar con el servidor")
