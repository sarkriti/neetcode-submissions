class Solution:

    def encode(self, strs: List[str]) -> str:
        #String length + delimeter + string
        res = []
        for word in strs: 
            res.append(str(len(word))) #Add the string length
            res.append("#")
            res.append(word)
        return "".join(res) #Join string list elements into a single string



    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        #Need to locate delimeter 
        i = 0
        
        while i < len(s): 
            j = i
            while s[j] != '#': #While curr char not delimeter
                j+=1 #Go to next char in string
            length = int(s[i:j]) #Extracting string length
            i = j + 1 #Go to char after #; Start of actual string
            j = i + length #End of the actual string
            decodedStrs.append(s[i:j]) #Extract actual string and add to list
            i = j #Have i be the end of the last extracted string
        return decodedStrs

                
