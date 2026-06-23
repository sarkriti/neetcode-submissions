class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for j in nums:
            if j in hashmap:
                return True
            else:
                hashmap[j] = 1
        return False
        