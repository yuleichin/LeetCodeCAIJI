#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: Yolay
@license: Apache Licence  
@contact: yuleichin@126.com
@software: PyCharm 
@file: array66.py 
@time: 10/09/2017 21:13 
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1:
            a = digits[0]
            a += 1
            a1 = a / 10
            b1 = a % 10
            if a1 != 0:
                return [1, 0]
            else:
                return [b1]
        else:
            total = 0
            for i in range(len(digits)):
                j = len(digits) - i - 1
                curr = digits[j] * (10 ** i)
                total += curr
            total += 1
            modTotal = total
            results = []
            while modTotal != 0:
                lastDigit = modTotal % 10
                results.insert(0, lastDigit)
                modTotal = modTotal / 10
            return results

