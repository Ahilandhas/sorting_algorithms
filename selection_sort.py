def selection_sort(arr:list) -> list:
    n = len(arr)

    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            arr[i],arr[min] = arr[min],arr[i]

    return arr


arr = [5,4,2,-1,1]
print(selection_sort(arr))
