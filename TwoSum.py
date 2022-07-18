
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Two Sum Solution to use in Leetcode"""
        index = sorted(range(len(nums)), key=lambda k: nums[k])
        nums = sorted(nums)
        leftpointer = 0
        rightpointer =len(nums) - 1
        while leftpointer < rightpointer:
            if nums[leftpointer] + nums[rightpointer] == target:
                return [index[leftpointer], index[rightpointer]]
            elif nums[leftpointer] + nums[rightpointer] < target:
                leftpointer += 1
            else:
                rightpointer -= 1

print(Solution().twoSum([3,2,4],6))