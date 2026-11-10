class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_seen = {}
        for i, n in enumerate(nums):
            if n not in dict_seen:
                dict_seen[target-n] = i
            else:
                return[dict_seen[n], i]