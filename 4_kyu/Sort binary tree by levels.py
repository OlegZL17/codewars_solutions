"""
DESCRIPTION:
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

Your task is to return the list with elements from tree sorted by levels,
which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
"""


def tree_by_levels(node):
    levels = {}
    result = []

    def tree_levels(node, level=1):
        if not node: return
        try:
            levels[level].append(node.value)
        except:
            levels[level] = [node.value]
        if node.left:
            tree_levels(node.left, level + 1)
        if node.right:
            tree_levels(node.right, level + 1)

    tree_levels(node)
    for i in levels.values():
        result += i

    return result