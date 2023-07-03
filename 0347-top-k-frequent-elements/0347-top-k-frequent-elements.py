class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i in nums:
            hash_dict[i] = hash_dict.get(i,0) + 1
        # sort the dict with values
        print(hash_dict)
        new_dict = sorted(hash_dict,key=lambda x:hash_dict[x],reverse=True)
        print(new_dict)
        return new_dict[:k]
