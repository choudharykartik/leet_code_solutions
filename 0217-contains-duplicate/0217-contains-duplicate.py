class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return True
            else:
                hash_set.add(i)
        else:
            return False