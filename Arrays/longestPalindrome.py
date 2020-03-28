class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestPalindrome=""
        for i in range(len(s)):
            temp=self.isPalindrome(s,i,i)
            if len(temp)>len(longestPalindrome):
                longestPalindrome=temp
            temp=self.isPalindrome(s,i,i+1)
            if len(temp)>len(longestPalindrome):
                longestPalindrome=temp    
        return longestPalindrome     
                
        
        
    def isPalindrome(self, s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
'''time complexity O(n^2) 
space O(1)'''             