class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        return_list = []
        for j in nums:
            if j in hashmap:
                hashmap[j]+= 1 #How you increment the value
            else:
                hashmap[j]= 1
        sorted_hashmap = sorted(hashmap.items(), key = lambda item: item[1], reverse= True)
        for i in range(k):
            return_list.append(sorted_hashmap[i][0])
        return return_list
            

            
        