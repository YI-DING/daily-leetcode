class Solution:
    def check(self,root):
        if not root:
            return True, 0
        if not root.left and not root.right:
            return True, 1
        left_flag, left_height = self.check(root.left)
        right_flag, right_height = self.check(root.right)
        if left_flag is False or right_flag is False:
            return False, max(left_height,right_height) + 1
        if abs(left_height - right_height) <= 1:
            return True, max(left_height,right_height) + 1
        else:
            return False, max(left_height,right_height) + 1
        
    def isBalanced(self, root: TreeNode) -> bool:
        flag, depth = self.check(root)
        return flag