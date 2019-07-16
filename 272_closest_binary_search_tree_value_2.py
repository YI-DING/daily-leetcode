def closestKValues(self, root, target, k):
    # write your code here
    def traverse(root):
        if not root:
            return []
        left = traverse(root.left)
        left.extend([root.val])
        right = traverse(root.right)
        left.extend(right)
        return left
        
    lst = traverse(root)
    if not lst:
        return []
    #find k closest nums
    pos = 0 if lst[0] == target else None
    for i in range(1, len(lst)):
        if lst[i-1] < target <= lst[i]:
            pos = i
            break
    pos = pos if pos else len(lst) - 1
    left, right = pos - 1, pos
    result = []
    
    for _ in range(k):
        if left < 0:
            result.append(lst[right])
            right += 1
        elif right > len(lst) - 1:
            result.append(lst[left])
            left -= 1
        elif abs(lst[left] - target) > abs(lst[right] - target):
            result.append(lst[right])
            right += 1
        else:
            result.append(lst[left])
            left -= 1
            
    return result