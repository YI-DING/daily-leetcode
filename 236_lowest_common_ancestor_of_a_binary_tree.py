def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    if p == root or q == root:
        return root
    
    left_result = self.lowestCommonAncestor(root.left,p,q)
    right_result = self.lowestCommonAncestor(root.right,p,q)
    
    if left_result and right_result:
        return root
    if left_result:
        return left_result
    if right_result:
        return right_result
    return None