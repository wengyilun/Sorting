# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    result = []
    # TO-DO
    while len(arrA) and len(arrB):
        if arrA[0] < arrB[0]:
            result.append(arrA.pop(0))
        else:
            result.append(arrB.pop(0))
        print(result)
    return result + arrA + arrB



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))





# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
