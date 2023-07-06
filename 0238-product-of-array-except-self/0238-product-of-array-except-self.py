class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]*len(nums)
        pre_prod = 1
        for i in range(1,len(nums)):
            pre_prod  *= nums[i-1]
            answer[i] = pre_prod
        post_prod = 1
        print(answer)
        for i in range(len(nums)-2,-1,-1):
            post_prod  *= nums[i+1]
            answer[i] *= post_prod
               
        return answer