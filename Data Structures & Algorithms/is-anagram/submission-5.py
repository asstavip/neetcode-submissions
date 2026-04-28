class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        seen = list(t)
        if len(t) != len(s) :
            return False
        
        for i in s:
            if i in seen:
                seen.remove(i)
        return len(seen) == 0