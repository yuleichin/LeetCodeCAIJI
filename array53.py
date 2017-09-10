#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: Yolay
@license: Apache Licence  
@contact: yuleichin@126.com
@software: PyCharm 
@file: array53.py 
@time: 10/09/2017 21:14 
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum