# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def double_dfs(node1:Optional[TreeNode],node2:Optional[TreeNode]) -> bool:
            # Base condition
            if not node1 and not node2:
                return True

            if node1 and node2 and node1.val != node2.val:
                return False
            elif not node1 or not node2:
                return False
            else:
                return double_dfs(node1.left,node2.left) and double_dfs(node1.right,node2.right)

        return double_dfs(p,q)
    