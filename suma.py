#sumar dos elementos los cuales los da el usuario 
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
print("QUE OPERACION DESEAS HACER :  ")
print("1- SUMA")
print("2- RESTA")
print("3- MULTIPLI")
print("4- DIV")

opcion = int(input("ingrese la opcion: "))
if opcion == 1: # los if se cierran con : dos puntos 
    suma=num1+num2
    print("la suma es: ",suma)
elif opcion == 2: # elif es la forma de hacer  lo igual a do-while o switch
    resta=num1-num2
    print("la resta es: ",resta)
elif opcion == 3:
    multi=num1*num2
    print("la multiplicacion es: ",multi)
elif opcion == 4:
    div=num1/num2
    print("la division es: ",div)
else:
    print("opcion invalida")

