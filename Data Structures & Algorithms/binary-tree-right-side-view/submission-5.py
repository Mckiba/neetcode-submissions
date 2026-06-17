# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        stack = collections.deque()
        stack.append([root, 0])
        res = [root.val]
        depth = 0
        rd = 0

        #[[1,0] ]
        #rd = 0
        #node  = 1, 0
        #res = [3]
        while stack:
            print(res)
            node,depth = stack.popleft()
            if node:
                if node.right and depth >= rd:
                    res.append(node.right.val)
                    stack.appendleft([node.left, depth + 1])
                    stack.appendleft([node.right, depth + 1])
                    rd = depth + 1

                elif node.left:
                    stack.append([node.right, depth + 1])
                    stack.append([node.left, depth + 1])
                    if depth >= rd:
                        res.append(node.left.val)
                    rd = depth + 1
                
        print(rd)
        return res 
