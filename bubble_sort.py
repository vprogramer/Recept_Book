def bubble_sort(arr):
    lenght = len(arr)

    for i in range(lenght-1):
        swapped = False
        for j in range(0, lenght-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break


arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)
print(arr)
