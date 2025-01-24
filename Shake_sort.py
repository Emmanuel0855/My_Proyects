def shakesort(arreglo):
    n = len(arreglo)
    l = 1
    r = n - 1
    k = n - 1
    while l < r:
        j = r
        while j > 0:
            if arreglo[j - 1] > arreglo[j]:
                aux = arreglo[j - 1]
                arreglo[j - 1] = arreglo[j]
                arreglo[j] = aux
                k = j
            j -= 1
        i = k + 1