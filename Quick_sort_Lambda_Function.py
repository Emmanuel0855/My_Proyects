quick_sort = lambda arr: arr if len(arr) <= 1 else \
    quick_sort([x for x in arr[1:] if x <= arr[0]]) + [arr[0]] + quick_sort([x for x in arr[1:] if x > arr[0]])
arr = [10, 5, 2, 3, 7, 8, 1, 9]
sorted_arr = quick_sort(arr)
print(sorted_arr)