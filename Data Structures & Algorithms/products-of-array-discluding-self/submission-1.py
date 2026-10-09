class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0
        res = []
        for i in nums:
                if i != 0:
                    product = product * i
                else:
                    zeroes+=1
        if zeroes > 1:
            res = [0] * (len(nums))
        elif zeroes ==1:
            zero_idx = nums.index(0)
            res = [0] * (len(nums))
            res[zero_idx] = product
        else:
            for j in nums:
                res.append(int(product/j))
        return res
        