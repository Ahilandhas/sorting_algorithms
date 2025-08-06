
def bubble_sort(arr:list) -> list:
    n = len(arr)

    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True

        if not swap:
            print("joi")
            return arr

    return arr


arr = [1,2,3,4,5]
print(bubble_sort(arr))
