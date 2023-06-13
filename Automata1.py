import re
#definimos la funcion del caracter
def caracter(caracter):
    global simbolo
    simbolo=""
    global Fin 
    Fin = ""
    digito="[0-9]"
    operador="(+|-|*|/)"
    #comparamos si el caracter es un operador 
    if re.match(digito,caracter):
        simbolo="Digito"
        return 0
    else:
 #comprobamos si es dig o operador 
        if re.match(digito,caracter):
            simbolo = " Operador "
            return 1
        #si no es digito nu operador es un cararter invalido 
        else:
            if(caracter==Fin):
                return 2
        print("Error el (caracter) no es valido ")
        exit()
#difinimos la funcion encabezado 
def encabezado():
    print("""| Edo. Actual |Caracter | Simbolo | Edo Siguiente""")
    body()

#definimos la funcion del contenido donde guarda cada valor
def contenido(estadosig, caracter, simbolo, estado):
    print("""|    ",estadosig,"    | ",caracter,"  |"simbolo,"  |   ",estado,"    |""")
    body()

#solo mostrar la linea que se manda a llamar
def body():
    print("+-----------+--------------+--------------+-------------")

#main
#tabla de trnciciones de automatas
tabla=[[1,"E","E"],[1,2,"E"],[3,"E","E"],[3,2,"A"]]
estado = 0

print("""+-------------------------------------+
----------------Ingresa la cadena a evaluar-----+
-----------------------------------------------+""")
cadena = input()
body()
encabezado()

#ciclo para recorrer la cadena 
for character in cadena:
    estadosig=estado
    #llamamos al metodo para revisar si es un cararcter valid
    character = caracter(character)

#guardamos el valor obtenido 
estado=tabla[estado][character]

#si el valor obtenido es E imprimimos cadena no valida 
if (estado =="E"):
    print("""|    ",estadosig,"    | ",caracter,"  |"simbolo,"  |   ",estado,"    |""")
    print("""------------------------Cadena no valida--------------------------""")
    exit()

contenido(estadosig,character,simbolo,estado)

#si el estado no es 3 imprimimos no valido

#if ( estado! == 3):
if (estado == 3):
    print("|    ",estado,"  |       |   FND     |       |")
    body()
    print("Cadena valida ")






















