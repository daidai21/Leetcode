# Runtime: 92 ms, faster than 69.50% of Python3 online submissions for Reconstruct Itinerary.
# Memory Usage: 14.3 MB, less than 7.69% of Python3 online submissions for Reconstruct Itinerary.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            targets[a] += [b]
        route = []
        def visit(airport):  # dfs
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]
