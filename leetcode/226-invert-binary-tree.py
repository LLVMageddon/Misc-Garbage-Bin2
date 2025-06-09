from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root: Optional[TreeNode] ) -> Optional[TreeNode]:

        if root is None:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp
        temp = None # this is not c/cpp

        self.invertTree(root.right)
        self.invertTree(root.left)
        return root




def list_to_tree(values : Optional[list[int]]) -> Optional[TreeNode]:
    # Note to self
    # I just have to write this to do this problem.
    # I think its time to create a leetcode account.
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()

        # Left
        if index < len(values) and values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1

        # Right 
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1

    return root

def tree_to_list(root: Optional[TreeNode]) -> Optional[List[int]]:
    # Note to self
    # I just have to write this to do this problem.
    # I think its time to create a leetcode account.
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # # Remove Nones children 
    while result and result[-1] is None:
        result.pop()

    return result





p = Solution()

input : list[int] = [2,1,3]
x = p.invertTree(list_to_tree(input))
print(tree_to_list(x))

input : list[int] = [4,2,7,1,3,6,9]
x = p.invertTree(list_to_tree(input))
print(tree_to_list(x))

input : list[int] = []
x = p.invertTree(list_to_tree(input))
print(tree_to_list(x))






