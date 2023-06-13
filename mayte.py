# Definimos una regla
rule1 = ("p= Manolo es cariñoso", "q=Manolo es amable")

# Definimos un hecho
fact1 = ("p",)

# Definimos un objetivo
goal1 = ("q",)

# Combinamos la regla y el hecho para verificar el objetivo
if set(rule1).issubset(set(fact1)):
    print("La regla y el hecho combinados cumplen el objetivo")
else:
    print("La regla y el hecho combinados no cumplen el objetivo")