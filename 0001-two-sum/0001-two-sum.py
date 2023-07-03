class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapping:
                return [i,mapping[diff]]
            mapping[nums[i]]=i
