from math import inf
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return True, inf, -inf
            if root.left:
                left_flag, leftmin, leftmax = helper(root.left)
            else:
                left_flag, leftmin, leftmax = True, root.val, root.val - 1
            if root.right:
                right_flag, rightmin, rightmax = helper(root.right)
            else:
                right_flag, rightmin, rightmax = True, root.val+1, root.val
            if left_flag and right_flag and leftmax < root.val < rightmin:
                return True, leftmin, rightmax
            else:
                return False, -inf, inf
        result, minn, maxx = helper(root)
        return result