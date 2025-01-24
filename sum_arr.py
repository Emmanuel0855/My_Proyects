def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + sum_array(arr, n-1)

arr = [2, 4, 6, 8, 10]
result = sum_array(arr, len(arr))
print(result)