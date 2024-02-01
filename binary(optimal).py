from math import log2
from math import ceil

class binaryTree:
    # i-th node - > 2i + 1; 2i + 2
    # i-th node <- (i - 1) // 2
    def __init__(self, arr):
        self.__data = arr
        self.depth = ceil(log2(len(arr) + 1))
        diff = 2**self.depth - 1 - len(arr)
        for i in range(diff):
            self.__data.append(None)

    def __getitem__(self, y, x):
        index = 2 ** y + x - 1
        return self.__data[index]

    def __str__(self):
        res = ""
        currentIndexes = [0]
        for y in range(self.depth):
            currentWidth = 2**y
            for x in range(currentWidth):
                res += str(self.__getitem__(y, x)) + " "
            res += "\n"
        return res

    @property
    def parent(self, index):
        return (index - 1) // 2

    @property
    def children(self, index):
        return (2 * index + 1, 2 * index + 2)

    """
    def sort(self):
        for i in reversed(range(self.depth)):
            for j in range(i)
    """


arr = [108, 123, 124, 135, 285, 379, 456, 476, 756, 998]
tree = binaryTree(arr)
print(tree.depth)
print(tree)