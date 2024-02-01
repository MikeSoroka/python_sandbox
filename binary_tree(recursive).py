class binaryTree:
    def __init__(self, val, left, right):
        self.root = val
        self.leftBranch = left
        self.rightBranch = right
        if None in (left, right):
            self.depth = 2
        else:
            self.depth = 1 + max(left.depth, right.depth)

    def __str__(self):
        res = ""
        currentTrees = [self]
        while None not in currentTrees:
            copy = currentTrees
            currentTrees = []
            for tree in copy:
                res += str(tree.root) + " "
                currentTrees.append(tree.leftBranch)
                currentTrees.append(tree.rightBranch)
            res += "\n"
        for leaf in currentTrees:
            res += str(leaf) + " "
        res += "\n"
        return res

    @property
    def nodes(self):
        return 2**(self.depth) - 1

def arrToTree(arr):
    if len(arr) == 1:
        res = binaryTree(arr[0], None, None)
    elif len(arr) == 2:
        res = binaryTree(arr[0], arr[1], None)
    elif len(arr) == 3:
        res = binaryTree(arr[0], arr[1], arr[2])
    else:
        midIndex = len(arr) // 2
        res = binaryTree(arr[0], arrToTree(arr[1:midIndex + 1]), arrToTree(arr[midIndex + 1:]))

    return res

arr = [108, 123, 124, 135, 285, 379, 456, 476, 756, 998]
test = arrToTree(arr)
print(test)
print(test.depth)
