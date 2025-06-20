from selection_sort.selection_sort import my_values


def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    #BUBBLE SORT
    n=len(unsorted_list)

    for i in range(n):
        for j in range(i+1,n):
            if unsorted_list[j]>unsorted_list[j+1]:
                unsorted_list[j],unsorted_list[j+1]=unsorted_list[j+1],unsorted_list[j]

#List to sort:
    my_values=[18,76,62,19,25]
    bubble_sort(my_values)


    pass
