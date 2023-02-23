# Longest increasing subsequence in nlgn
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                ind = bisect_left(ans, nums[i])
                ans[ind] = nums[i]
        return len(ans)