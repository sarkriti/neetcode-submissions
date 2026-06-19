class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Extract substring that removes special characters and have it all be lower case
        clean_string = "".join(char for char in s if char.isalnum()).lower()
        
        l,r = 0, len(clean_string)-1

        while(l<r):
            if clean_string[l] != clean_string[r]:
                return False
            l+= 1
            r -= 1
        return True

        