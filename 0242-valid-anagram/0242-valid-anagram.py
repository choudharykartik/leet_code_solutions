class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sd,td = {},{}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sd[s[i]] = sd.get(s[i],0)+1
            td[t[i]] = td.get(t[i],0)+1
        if sd == td:
            return True
        else:
            return False
        