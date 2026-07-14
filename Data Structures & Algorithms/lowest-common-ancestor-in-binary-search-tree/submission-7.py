# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Here the idea is to use the property of BST where the left chils is
        < and the right one is >. We can explore through a dfs the tree while
        checking wrt p and q if the current node can eventually be an ancestor
        and if we can go over.

        we don't care about passing p and q to the dfs, they're part of the outer
        scope so they can be accessed (no need to modify them).

        If you go left, then the node must be lower
        """
        if not root or not p or not q:
            return None


        def dfs(node: Optional[TreeNode])->Optional[TreeNode]:
            # Base condition
            if not node:
                return None

            if  p.val < node.val and q.val < node.val:
                return dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else:
                return node
            
        return dfs(root)

