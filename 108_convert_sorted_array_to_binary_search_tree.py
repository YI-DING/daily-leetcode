# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        if not nums:return None 
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        if mid>0:
            root.left=Solution.sortedArrayToBST(self,nums[:mid])
        if mid<len(nums)-1:
            root.right=Solution.sortedArrayToBST(self,nums[mid+1:])
        return root
#dont have to use if statement as when nums get null value it still works
