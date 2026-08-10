from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def safe(n):
            if n: return n.val
            else: "N/A"
        
        if not root: return []
        
        q = deque([(root, 0)])
        res = []
        layer = []
        curr_depth = 0
        while q:
            node, depth = q.popleft()
            # print(depth, "|", safe(node.left), node.val, safe(node.right))
            if depth > curr_depth:
                curr_depth += 1
                res.append(layer)
                layer = []
            layer.append(node.val)
            if node.left:  q.append((node.left, curr_depth + 1))
            if node.right: q.append((node.right, curr_depth + 1))
            # print("queue: [", end="")
            # for node, _ in q:
                # print(node.val, end=", ")
            # print("]")

        res.append(layer)
        return res