class Solution:
    def hasDuplicate(self, nums):
        s = set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True