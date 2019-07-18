def findTilt(self, root: TreeNode) -> int:
    self.tilt = 0
    def summ(root):
        if not root:
            return 0
        return root.val + summ(root.left) + summ(root.right)
    def find(root):
        if not root:
            return 
        self.tilt += abs(summ(root.left) - summ(root.right))
        find(root.left)
        find(root.right)
        return 
    find(root)
    return self.tilt
#solution from @jiuzhang.com:
class Solution:
    """
    @param root: the root
    @return: the tilt of the whole tree
    """

    def findTilt(self, root):
        # Write your code here
        return self.countTree(root)[1]

    def countTree(self, root):
        if not root:
            return 0, 0
        l_sum, l_answer = self.countTree(root.left)
        r_sum, r_answer = self.countTree(root.right)
        return root.val + l_sum + r_sum, l_answer + r_answer + abs(l_sum - r_sum)