class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aset = set()
        lf = 0
        maxlen = 0
        for i in range(len(s)):
            while s[i] in aset:
                aset.remove(s[lf])
                lf+=1
            aset.add( s[i])
            maxlen = max(maxlen, i-lf+1)
        return maxlen

        
               


        