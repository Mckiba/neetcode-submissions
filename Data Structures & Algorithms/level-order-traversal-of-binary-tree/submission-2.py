# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = defaultdict(list)
        stack = [[root, 1]]

        while stack:
            node,depth = stack.pop()

            if not node:
                continue

            res[depth].append(node.val)

            val = []

            if node:
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])


        return list(res.values())


         

        
        