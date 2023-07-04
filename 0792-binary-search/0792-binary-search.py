class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l,r, = 0,n-1
        while l<=r:
            print(l,r)
            mid = l+(r-l)//2
            if nums[mid]<target:
                l = mid+1
                continue
            if nums[mid]>target:
                r=mid-1
                continue
            if nums[mid] == target:
                return mid
        return -1
