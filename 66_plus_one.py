class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string=""
        for num in digits:
            string+=str(num)
        return [int(digit) for digit in str(1+int(string))]