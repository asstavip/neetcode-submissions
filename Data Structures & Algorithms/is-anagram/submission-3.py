class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seen = list(s)
        lis = t
        if len(t) > len(s):
            seen = list(t)
            lis = s
        for i in lis:
            if i in seen:
                seen.remove(i)
        return len(seen) == 0