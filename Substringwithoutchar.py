"Use sliding window technique"


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        charseen={}
        count=start=0
        for i in range(len(s)):
            if s[i] in charseen and start<=charseen[s[i]]:
                start=charseen[s[i]]+1
            else:
                count=max(count,i-start+1)
            charseen[s[i]]=i    
        return count
        print(charseen)



''' Input:"abcabcbb"
charseen={a:0,b:1,c:2}= dictionary wil be like this
start point will get updated each time if value found in dictionary

Time complexity : O(n). Index i will iterate n times.

Space complexity (dictionary) : O(min(m, n))'''       