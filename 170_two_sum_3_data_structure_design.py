'''
If we use hash table, add() takes O(1), find() takes O（n) time, O(n) space.
If we use table and two pointers, add takes O(1), find() takes O(nlogn) time, inplace.
'''
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.dicc = {}

    def add(self, number):
        # write your code here
        if number in self.dicc:
            self.dicc[number] += 1
        else:
            self.dicc[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for number in self.dicc:
            if (value - number in self.dicc and 
            (value - number != number or self.dicc[number] > 1)):
                return True
        return False