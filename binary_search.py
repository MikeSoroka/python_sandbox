def binary_search(arr, el, start=0, end=-1):
    left = start
    if end == -1:
        right = len(arr) - 1
    else:
        right = end
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == el:
            return mid
        elif arr[mid] > el:
            right = mid - 1
        else:
            left = mid + 1
    if arr[left] == el:
        return left
    else:
        return -1

"""
libraryNum = [108, 123, 124, 135, 285, 379, 456, 476, 756, 998]
print(binary_search(libraryNum, 285))
print(binary_search(libraryNum, 285, 4, 7))
print(binary_search(libraryNum, 285, 1, 4))
print(binary_search(libraryNum, 285, 5))
"""
