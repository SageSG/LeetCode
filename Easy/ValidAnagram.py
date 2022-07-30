class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = True
        object_of_letters = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if not char in object_of_letters.keys():
                object_of_letters[char]=1
            else:
                object_of_letters[char]+=1
                
        for char in t:
            if char in object_of_letters.keys():
                object_of_letters[char] -= 1
                if object_of_letters[char] < 0:
                    is_anagram = False
                    break
            else:
                is_anagram = False
                break
        
        if not is_anagram:
            return False
        
        return True
print(Solution.isAnagram(Solution, "rat", "car"))