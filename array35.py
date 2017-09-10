#!/usr/bin/env python  
# encoding: utf-8
""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: yuleichin@126.com
@software: PyCharm 
@file: array35.py 
@time: 10/09/2017 16:24 
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 这题也主要是考察对于newTail的使用，前提是有序数组
        if not nums:
            return 0
        newTail = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                newTail += 1
            else:
                return newTail
        return newTail
