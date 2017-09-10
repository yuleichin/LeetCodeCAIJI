#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: Yolay
@license: Apache Licence  
@contact: yuleichin@126.com
@software: PyCharm 
@file: array532.py 
@time: 10/09/2017 20:43 
"""
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        kpair = 0
        alreadyk = []
        #nums = list(set(nums))
        for i in range(0, len(nums)-1):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                if abs(nums[j]-curr) == k:
                    if ([curr, nums[j]] in alreadyk):
                        continue
                    else:
                        kpair += 1
                        alreadyk.append([curr, nums[j]])
                        alreadyk.append([nums[j], curr])
        return kpair
        '''
        '''
        if k < 0: return 0
        c = collections.Counter(nums)
        return sum(c[n + k] > 1 - bool(k) for n in c.keys())
        '''
        if k < 0:
            return 0
        res = 0
        n = len(nums)
        j = 0
        i = 0
        nums.sort()
        while i < n:
            j = max(j, i+1)
            while j < n and nums[j] - nums[i] < k:
                j += 1
            if j<n and nums[j]- nums[i] == k:  # 只取第一次相等的时候增加res
                res += 1
            while i < n-1 and nums[i] == nums[i+1]:   # 删掉前面重复的元素
                i += 1
            i += 1
        return res