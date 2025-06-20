def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    arr = unsorted_list.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    # values to sort:
my_values = [20, 18, 28, 65, 75]

selection_sort(my_values)
print("Sorted list:", my_values)

    pass
