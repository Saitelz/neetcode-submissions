class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_num = set(nums)
        best = 0

        for n in set_of_num:
            if n - 1 not in set_of_num:
                length = 1
                while n + length in set_of_num:
                    length += 1
                best = max(best, length)

        return best