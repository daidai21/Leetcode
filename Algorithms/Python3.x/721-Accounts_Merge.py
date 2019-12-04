# union-find
# Runtime: 280 ms, faster than 35.30% of Python3 online submissions for Accounts Merge.
# Memory Usage: 16.5 MB, less than 100.00% of Python3 online submissions for Accounts Merge.
class DSU(object):
    def __init__(self):
        self.parents = list(range(10001))

    def find(self, x):
        if self.parents[x] != x:  # path compress
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name, email_to_id = {}, {}
        id_ = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = id_
                    id_ += 1
                dsu.union(email_to_id[account[1]], email_to_id[email])
        answer = collections.defaultdict(list)
        for email in email_to_name:
            answer[dsu.find(email_to_id[email])].append(email)
        return [[email_to_name[value[0]]] + sorted(value) for value in answer.values()]
