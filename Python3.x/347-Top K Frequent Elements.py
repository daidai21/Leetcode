# heap and hash
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k: return   # judge error
        hash = {}
        for num in nums:
            if num in hash: hash[num] += 1
            else: hash[num] = 1
        heap = []
        for num, frequent in hash.items():
            heapq.heappush(heap, (-1 * frequent, num))  # heapq本身是小根堆、乘-1转为大根堆
        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result
