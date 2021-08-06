# Python program for implementation of Selection Sort

A = [64, 34, 25, 12, 22, 11, 90]

# # Traverse through all array elements
# for i in range(len(A)):
#
#     # Find the minimum element in remaining
#     # unsorted array
#     min_idx = i
#     for j in range(i + 1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j
#
#     # Swap the found minimum element with
#     # the first element
#     A[i], A[min_idx] = A[min_idx], A[i]
#
# # Driver code to test above
# print("Sorted array")
# print(A)


def selectionSort(data):
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex
        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]


selectionSort(A)
print(A)
