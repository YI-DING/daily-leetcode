def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    dicc = {}
    def traverse(root,dicc):
        if not root:
            return None
        leftsum = traverse(root.left,dicc) if root.left else 0
        rightsum = traverse(root.right,dicc) if root.right else 0
        rootsum = leftsum + rightsum + root.val
        if rootsum not in dicc:
            dicc[rootsum] = 1
        else:
            dicc[rootsum] += 1
        return rootsum
    traverse(root,dicc)
    maxx, result = 0, []
    for summ,freq in dicc.items():
        if freq > maxx:
            maxx = freq
            result = [summ]
        elif freq == maxx:
            result.append(summ)
    return result