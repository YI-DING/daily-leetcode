class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def traverse(root):
            if not root or not root.left and not root.right:
                return 0,0
            left_depth, left_dia = traverse(root.left)
            right_depth, right_dia = traverse(root.right)
            if not root.left:
                return right_depth + 1, max(right_depth + 1, right_dia)
            if not root.right:
                return left_depth + 1, max(left_depth + 1, left_dia)
            depth = max(left_depth, right_depth) + 1
            dia = max(left_depth + right_depth + 2, left_dia, right_dia)
            return depth, dia
        return traverse(root)[1]
