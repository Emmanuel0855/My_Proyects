def bubble_sort(arreglo):
    n = len(arreglo)
    for i in range(n, 0, -1):
        for j in range(i - 1):
            if arreglo[j] > arreglo[j + 1]:
            #Intercambiar elementos
                aux = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = aux

arreglo = [5, 2, 9, 1, 5, 6]
bubble_sort(arreglo)
print(arreglo)