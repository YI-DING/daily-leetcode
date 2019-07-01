# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) :
        if not root:return True 
        if not root.left and not root.right:return True
        leftstack=[]
        rightstack=[]
        
        def left_traverse(root):
            if not root:leftstack.append(None)
            else:
                if root.left or root.right:
                    left_traverse(root.left)
                    left_traverse(root.right)
                    leftstack.append(root.val)
                else:leftstack.append(root.val)
        def right_traverse(root):
            if not root:rightstack.append(None)
            else:
                if root.left or root.right:
                    right_traverse(root.right)
                    right_traverse(root.left)
                    rightstack.append(root.val)
                else:rightstack.append(root.val)
        if root.left and root.right:
            left_traverse(root.left)
            right_traverse(root.right)
        else:return False
        return True if leftstack==rightstack else False 
    '''
    def isSymmetric(self, root):
        def isSym(L,R):
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        return not root or isSym(root.left, root.right)'''
    '''
    def isSymmetric(self, root):
    queue = [root]
    while queue:
        values = [i.val if i else None for i in queue]
        if values != values[::-1]: return False
        queue = [child for i in queue if i for child in (i.left, i.right)]
    return True'''
    '''
    def isSymmetric(self, root):
    def sym_tree(L,R):
        if L and R: 
            return L.val == R.val and sym_tree(L.left, R.right) and sym_tree(L.right, R.left)
        else:
            return L == R
    return sym_tree(root, root)
    '''
    '''
    def isSymmetric(self, root):
    now = []
    if root:
        now.append(root)
    while now:
        vals = []
        for i in now:
            if i:
                vals.append(i.val)
            else:
                vals.append(None)
        if list(reversed(vals)) != vals:
            return False
        else:
            now = [j for i in now if i for j in (i.left, i.right)]
    return True
    '''
    '''
    def isSymmetric(self, root):
    if not root:
        return True

    dq = collections.deque([(root.left,root.right),])
    while dq:
        node1, node2 = dq.popleft()
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        # node1.left and node2.right are symmetric nodes in structure
        # node1.right and node2.left are symmetric nodes in structure
        dq.append((node1.left,node2.right))
        dq.append((node1.right,node2.left))
    return True
    '''
    '''
     class Solution2:
  def isSymmetric(self, root):
    if root is None:
      return True

    stack = [[root.left, root.right]]

    while len(stack) > 0:
      pair = stack.pop(0)
      left = pair[0]
      right = pair[1]

      if left is None and right is None:
        continue
      if left is None or right is None:
        return False
      if left.val == right.val:
        stack.insert(0, [left.left, right.right])

        stack.insert(0, [left.right, right.left])
      else:
        return False
    return True
    '''