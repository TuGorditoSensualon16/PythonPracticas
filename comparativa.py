caracteristicas = ""

respuestas = input("¿Eres alta o baja? 1, 2: ")
if respuestas == "1":
    caracteristicas += "alta"
    respuestas = input("¿Eres morena o rubia? 1, 2: ")
    if respuestas == "1":
        caracteristicas += ", morena"
        respuestas = input("¿Eres buena o mala programando? 1, 2: ")
        if respuestas == "1":
            caracteristicas += ", buena programando"
        else:
            caracteristicas += ", mala programando"
    else:
        caracteristicas += ", wuera"
        respuestas = input("¿Eres buena o mala programando? 1, 2: ")
        if respuestas == "1":
            caracteristicas += ", buena programando"
        else:
            caracteristicas += ", mala programando"
else:
    caracteristicas += "baja"
    respuestas = input("¿Eres morena o wuera? 1, 2: ")
    if respuestas == "1":
        caracteristicas += ", morena"
        respuestas = input("¿Eres buena o mala programando? 1, 2: ")
        if respuestas == "1":
            caracteristicas += ", buena programando"
        else:
            caracteristicas += ", mala programando"
    else:
        caracteristicas += ", rubia"
        respuestas = input("¿Eres buena o mala programando? 1, 2: ")
        if respuestas == "1":
            caracteristicas += ", buena programando"
        else:
            caracteristicas += ", mala programando"

print("Tus características son:", caracteristicas, "Eres gato :v")




