# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:Optional[TreeNode])->Tuple[int,bool]:
            if not node:
                return (0,True)

            left,check_left = dfs(node.left)
            right,check_right = dfs(node.right)

            if not check_left or not check_right or not (right - 1 <= left <= right +1):
                return (0,False)
            else:
                return (max(left,right)+1,True)

        _,res = dfs(root)
        return res
            