class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        top_list = sorted(counts.items(), key=lambda x: -x[1])[:k]


        return [top_list[i][0] for i in range(len(top_list))]