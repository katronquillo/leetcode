class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Construct hashmap of character occurrences in magazine
        magChars = {}
        for char in magazine: 
            if (char not in magChars):
                magChars[char] = 0
            magChars[char] += 1
        
        # Iterate through the note
        for char in ransomNote:
            if (char not in magChars):
                return False
            else:
                magChars[char] -= 1
                if (magChars[char] == 0):
                    del magChars[char]
        
        return True