class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_n = set(nums)

        if len(set_n) < len(nums):
            return True
        else:
            return False