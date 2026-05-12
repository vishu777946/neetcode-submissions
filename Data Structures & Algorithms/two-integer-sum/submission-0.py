class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for l in range(len(nums)):
            for i in range(l + 1, len(nums)):
                if target - nums[i] == nums[l] or target - nums[l] == nums[i]:
                    return [l,i]