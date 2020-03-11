"""
3.	Design a  binary tree and then print the breadth first order traversal of this tree. In breadth first order traversal,
    we visit the nodes of same height first then go to nodes of next height or level
"""

class Binary_Tree:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def levelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        givenLevel(root, i)

def givenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print("%d" % (root.data))
    elif level > 1:
        givenLevel(root.left, level - 1)
        givenLevel(root.right, level - 1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

root = Binary_Tree(1)
root.right=Binary_Tree(2)
root.right.right=Binary_Tree(5)
root.right.right.left=Binary_Tree(3)
root.right.right.right=Binary_Tree(6)
root.right.right.left.right=Binary_Tree(4)

levelOrder(root)