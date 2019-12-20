# DFS
# Runtime: 260 ms, faster than 5.46% of Python3 online submissions for Employee Importance.
# Memory Usage: 17.1 MB, less than 8.33% of Python3 online submissions for Employee Importance.
"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {employee.id: employee for employee in employees}
        employee = dic[id]
        total_importance = employee.importance
        for id in employee.subordinates:
            total_importance += self.getImportance(employees, id)
        return total_importance


# BFS
# Runtime: 148 ms, faster than 98.91% of Python3 online submissions for Employee Importance.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Employee Importance.
"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {employee.id: employee for employee in employees}
        total_importance = 0
        stk = [dic[id]]
        while stk:
            employee = stk.pop()
            total_importance += employee.importance
            for id in employee.subordinates:
                stk.append(dic[id])
        return total_importance
