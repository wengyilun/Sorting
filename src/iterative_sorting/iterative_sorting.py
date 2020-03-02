# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # TO-DO: find next smallest element
        current_index = i
        smallest_index = current_index
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[current_index]
        arr[current_index] = temp
        # TO-DO: swap
    print(arr)
    return arr


'''
selection_sort - Version 2 
'''
def find_smallest_index(arr):
    smallest_index = 0
    for i in range(0, len(arr)):
        current_index = i
        if arr[current_index] < arr[smallest_index]:
            smallest_index = current_index

    return smallest_index


def selection_sort2(arr):
    result = []
    for i in range(0, len(arr)):
        smallest_index = find_smallest_index(arr)
        result.append(arr.pop(smallest_index))

    return result

#selection_sort([4, 5, 2, 3])
#selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
#selection_sort([])
#selection_sort([0, 1, 2, 3, 4, 5])

#find_smallest_index([9,6,3,2,7,5,1])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                print(arr[i])
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = True

    print(arr)
    return arr

#bubble_sort([1, 5, 8, 4])
#bubble_sort([8, 3, 7, 1, 6])


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr