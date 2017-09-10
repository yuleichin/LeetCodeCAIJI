# -*- coding: utf-8 -*
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## the array is sorted
        # 这个题目也是用newTail这样一个技巧来排除相同元素
        # 但是是建立在这个是有序数组的基础上
        if not nums:
            return 0
        newTail = 0
        total = len(nums)
        for i in range(1, total):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail + 1