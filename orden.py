def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Pedir al usuario que ingrese los números enteros separados por espacios
nums = input("Ingrese los números enteros separados por espacios: ")

# Convertir los números ingresados a una lista de enteros
num_list = [int(x) for x in nums.split()]

# Ordenar la lista de enteros de menor a mayor
sorted_list = selection_sort(num_list)

# Imprimir la lista ordenada
print("Los números ordenados de menor a mayor son:", sorted_list)
