class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(i)
        return res.values()