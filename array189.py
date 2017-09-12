#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: Yolay
@license: Apache Licence  
@contact: yuleichin@126.com
@software: PyCharm 
@file: array189.py 
@time: 12/09/2017 19:48 
"""
from copy import deepcopy
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        total = len(nums)
        actual_k = k%total
        temp = deepcopy(nums[-actual_k:])
        nums[actual_k:] = nums[0:-actual_k]
        nums[0:actual_k] = temp
        # 用了余数的概念，本题用Python解比较简单