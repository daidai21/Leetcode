# dp
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        for num in nums:
            i, j = max(i, j), i + num
        return max(i, j)


'''
令dp[i]表示在之前i个房间中所能拿到最多的钱，i=nums.size()时，即所求。 
则，dp[0] = 0表示不抢
dp[1]=nums[0]，表示在前一个房间抢到最多的钱数；
dp[2]=max{nums[0],nums[1]}，表示在前两个房间抢到最多的钱数；
dp[3]=max{nums[0],nums1,nums[2],num[0]+num[2]}=max{nums1,num[0]+num[2]}
由此递推可知dp[i]=max{dp[i−1],dp[i−2]+nums[i]} 
'''
