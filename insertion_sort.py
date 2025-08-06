def insertion_sort(arr:list) -> list:
    n = len(arr)

    for i in range(1,n):
        pivot = arr[i]
        j = i-1
        while pivot < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = pivot
    return arr


arr = [5,4,2,-1,1]
print(insertion_sort(arr))
