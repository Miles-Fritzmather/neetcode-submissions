# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        if root.right is None and root.left is None: return TreeNode(root.val, None, None)
        if root.right is None: return TreeNode(root.val, None, self.invertTree(root.left))
        if root.left is None: return TreeNode(root.val, self.invertTree(root.right), None)
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))