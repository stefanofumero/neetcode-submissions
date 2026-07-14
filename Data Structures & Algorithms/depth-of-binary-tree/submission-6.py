# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(node: Optional[TreeNode],depth_counter):
            nonlocal max_depth

            if node == None:
                return

            max_depth = max(max_depth,depth_counter)

            dfs(node.left,depth_counter+1)
            dfs(node.right,depth_counter+1)
        
        dfs(root,1)
        return max_depth