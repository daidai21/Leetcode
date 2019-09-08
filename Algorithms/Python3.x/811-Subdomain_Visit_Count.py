# Runtime: 72 ms, faster than 11.89% of Python3 online submissions for Subdomain Visit Count.
# Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Subdomain Visit Count.
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = collections.Counter()
        for cd in cpdomains:
            n, d = cd.split(' ')
            c[d] += int(n)
            for i in range(len(d)):
                if d[i] == '.':
                    c[d[i + 1:]] += int(n)
        return ["{0} {1}".format(c[k], k) for k in c]
