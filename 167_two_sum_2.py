class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dicc={}
        for i,num in enumerate(numbers):
            if num in dicc:
                return[dicc[num],i+1]
            else:
                dicc.update({(target-num):i+1})
#dictionary(O(n),O(n)) did not use the info of 'sorted'!!!!!!!!!!
#two-pointer(O(n),O(1)) is not optimal
#BST is O(n),O(1).....
