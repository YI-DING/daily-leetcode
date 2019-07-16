def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
        return root
    elif root.val > max(p.val,q.val):
        return self.lowestCommonAncestor(root.left,p,q)
    else:
        return self.lowestCommonAncestor(root.right,p,q)