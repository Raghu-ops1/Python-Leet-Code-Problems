'''The get() method returns:
the value for the specified key if key is in dictionary.
None if the key is not found and value is not specified.
value if the key is not found and value is specified.

The syntax of get() is:

dict.get(key[, value]) 

get() Parameters
The get() method takes maximum of two parameters:
1.key - key to be searched in the dictionary
2.value (optional) - Value to be returned if the key is not found. The default value is None.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for w in strs:
            key=tuple(sorted(w))
            d[key]=d.get(key, [])+[w]
        return list(d.values())  

'''Time Complexity= O (n * m log (m))'''


