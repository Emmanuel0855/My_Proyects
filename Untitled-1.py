def product_of_array(arr, n):
    if n == 0:
        return 1  # Caso base, el producto de un vector vacío es 1
    return arr[n-1] * product_of_array(arr, n-1)

# Ejemplo:
arr = [2, 3, 4]
print(product_of_array(arr, len(arr)))  # Output: 24