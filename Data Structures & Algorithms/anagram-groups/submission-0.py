class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = {}
        #Iterate through the list 
        for i,j in enumerate(strs):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in anagram_group:
            #add the string to the word list 
                anagram_group[sorted_str].append(j)
            else:
                anagram_group[sorted_str]= [j]
        return list(anagram_group.values())