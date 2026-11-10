class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j, n in enumerate(nums[i+1:]):
                if n == target - nums[i]:
                    return [i, j+i+1] 