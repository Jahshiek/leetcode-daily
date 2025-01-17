class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = total_sum - leftSum - nums[i]
            if rightSum == leftSum:
                return i
            leftSum += nums[i]
        return -1

# 28 - 0  - 1 = 27
# 28 - 1 - 7 = 20
# 28 - 8 - 3 = 11
# 28 - 11 - 6 = 11