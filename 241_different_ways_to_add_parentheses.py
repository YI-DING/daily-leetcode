class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def difc(input):
            if "*" not in input and "-" not in input and "+" not in input:return([int(input)])
            else:
                return[left+right if mid=="+" else left-right if mid=="-" else left*right
                      for index,mid in enumerate(input) if mid in "+-*"
                      for left in difc(input[:index])
                      for right in difc(input[index+1:])] #or [int(input)]
        return difc(input)   
# since the left side would never be null but right might.