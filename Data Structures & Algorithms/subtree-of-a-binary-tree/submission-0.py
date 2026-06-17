# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        stack = [root]
        print(root)
        while stack:
            n = stack.pop()

            if not n:
                continue

            if self.isSameTree(n, subRoot):
                return True
            else:
                stack.append(n.left)
                stack.append(n.right)
        return False


        
        
    def isSameTree(self, p:Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
                return True

        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        


        
