"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
from collections import deque
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dicc = {emp.id:emp for emp in employees}
        if not employees:
            return 0
        start = [emp for emp in employees if emp.id == id]
        queue,total = deque(start),0
        while queue:
            emp = queue.popleft()
            total += emp.importance
            for sub in emp.subordinates:
                queue.append(dicc[sub])
        return total