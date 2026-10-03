class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #HashMap: Key - Number; Value - Count
        numCount = defaultdict(int)
        res = []
        for num in nums:
                numCount[num] += 1
        for _ in range(k):
            maxKey = max(numCount, key=numCount.get)
            res.append(maxKey)
            del numCount[maxKey]
        return res

        