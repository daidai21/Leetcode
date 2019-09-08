# Runtime: 92 ms, faster than 8.90% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for Unique Email Addresses.
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            temp = email.split('@')
            local_name = list(temp[0])
            for _ in range(local_name.count('.')):  # del .
                local_name.remove('.')
            if '+' in local_name:  # del +
                idx = local_name.index('+')
                local_name = local_name[:idx]
            res.add(str(local_name) + "@" + temp[1])
        return len(res)


# Runtime: 60 ms, faster than 66.02% of Python3 online submissions for Unique Email Addresses.
# Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for Unique Email Addresses.
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            # temp = email.split('@')
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.', '') + '@' + domain)
        return len(seen)
