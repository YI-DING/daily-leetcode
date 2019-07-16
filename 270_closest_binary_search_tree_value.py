def closestValue(self, root, target):
    if not root:
        return inf
    if root.val == target:
        return target
    if root.val > target:
        left = self.closestValue(root.left, target)
        return root.val if abs(root.val - target) < abs(left - target) else left
    if root.val < target:
        right = self.closestValue(root.right, target)
        return root.val if abs(root.val - target) < abs(right - target) else right
#iterative solution by @jiuzhang.com:
def closestValue(self, root, target):
    upper = root
    lower = root
    while root:
        if target > root.val:
            lower = root
            root = root.right
        elif target < root.val:
            upper = root
            root = root.left
        else:
            return root.val
    if abs(upper.val - target) <= abs(lower.val - target):
        return upper.val
    return lower.val