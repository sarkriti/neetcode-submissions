class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Cycle through strs
        # Sort strs value
        # If sorted strs value is not in hashmap then added
        #Hashmap Key: sorted string; Hashmap Value: the strs value 
        #Return the items in the hashmap

        anagramGroups = defaultdict(list)

        for currStr in strs:
            sortedStr = str(sorted(currStr))
            anagramGroups[sortedStr].append(currStr)
        return list(anagramGroups.values())


            
        