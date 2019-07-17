class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if not numbers:
            return None
        numbers.sort()

        def twosum(array, value):
            if not array:
                return []
            result = []
            start, end = 0, len(array) - 1
            while start < end:
                if array[start] + array[end] == target:
                    result.append([start, end])
                    lft, rgt = array[start], array[end]
                    while start < end and array[start] == lft:
                        start += 1
                    while start < end and array[end] == rgt:
                        end -= 1
                elif array[start] + array[end] > target:
                    end -= 1
                else:
                    start += 1
            return result

        start = 0
        result = []
        while start < len(numbers) - 2:
            twosum_result = twosum(numbers[start+1:], -numbers[start])
            for pair in twosum_result:
                result.append([numbers[start]] + pair)
            num = numbers[start]
            while start < len(numbers) -2 and num == numbers[start]:
                start += 1
        return result 