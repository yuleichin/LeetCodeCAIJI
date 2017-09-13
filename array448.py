#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: Yolay
@license: Apache Licence  
@contact: yuleichin@126.com
@software: PyCharm 
@file: array448.py 
@time: 12/09/2017 22:28 
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    # 本题很考验思想，找到缺失的数。如果给定数组不缺少，则应该给出的值为 1:N, 对应下标为0:N-1，长度为N
    # 若不缺，则index应该就是0,1,2,...,N-1.  假设缺少3，则会是0,1,1,3,...,N-1
    # 则nums[0[ = -1, nums[1] = -2, nums[1] = 2, nums[3] = -4....,缺少的地方由于多了出来而为正
    # 所以瞄准那些正的值，就对应着缺失的值

