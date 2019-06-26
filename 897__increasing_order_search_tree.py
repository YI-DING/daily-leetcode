# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode):
        print(f'{root.val} is what we are examining. Its left is {None if not root.left else root.left.val} and right is {None if not root.right else root.right.val}')
        if not root:return root
        if root.right:
            print(f'we are iBSTing {root.right.val}')
            root.right=Solution.increasingBST(self,root.right)
        if not root.left:
            print(f'{root.val} is done iBST')
            return root
        if not root.left.right:
            root.left.right=root
            print(f'we have lifted {root.left.val} and planted {root.val} to its right')
            return root.left
        left_subtree_right=root.left.right
        while True:
            if not left_subtree_right.right:
                left_subtree_right.right=root
                print(f'we have planted {root.val} to the right of {left_subtree_right.val}')
                return Solution.increasingBST(self,root.left)
            left_subtree_right=left_subtree_right.right

   def increasingBST(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res