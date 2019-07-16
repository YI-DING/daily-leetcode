def flatten(self, root):
    if not root or not root.left and not root.right:
        return 
    
    self.flatten(root.left)
    self.flatten(root.right)
    if not root.left:
        return 
    if not root.right:
        root.right = root.left
        root.left = None
        return
    
    pointer = root.left
    while pointer.right:
        pointer = pointer.right
    pointer.right = root.right
    root.right = root.left
    root.left = None
    return 