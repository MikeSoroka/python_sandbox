def bubble_sort(arr):
    #counter = 0
    for i in range(len(arr) - 1):
        permutationsDone = False
        for j in range(len(arr) - i - 1):
            #counter += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                permutationsDone = True
        if not permutationsDone:
            break
    #print(counter)

"""
libraryNum = [108,123,124,135,756,476,285,998,379,456]
print("Initial array:", libraryNum)
bubble_sort(libraryNum)
print("Sorted array:", libraryNum)
"""