# -*- coding: utf-8 -*
class Solution(object):
    # 这道题主要是采用newTail的技巧，控制前newTail个元素是符合题目要求的
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        newTail = -1
        for i in range(0,len(nums)):
            if nums[i] != val:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail + 1