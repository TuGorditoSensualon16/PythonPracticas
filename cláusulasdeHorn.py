rule1 = ("p= Manolo es cariñoso", "q= Manolo es amable")

fact1 = ("p",)
#definir la meta 
goal1 = ("q",)

#Combinar la regla y el hecho para comprobar el gol
if set(rule1).issubset(set(fact1)):
    print("La regla y el hecho combinados cumplen el objetivo")
else:
    print("La regla y el hecho combinados no cumplen el objetivo")
