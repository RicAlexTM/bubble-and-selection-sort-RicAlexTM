def selection_sort(arr):
    n=len(arr)
    #Outer loop searching for the smallest number putting it in index i
    for i in range(n):
        min_index = i
        # Inner loop searching for the smallest number from remaining list putting it in index j
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
                #Swapping the smallest value with the value at i
                arr[i], arr[min_index]=arr[min_index],arr[i]

#values to sort:
my_values = [20, 18, 28, 65, 75]

selection_sort(my_values)
print("Sorted list:",my_values)


pass
