#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: Yolay
@license: Apache Licence  
@contact: yuleichin@126.com
@software: PyCharm 
@file: array118.py 
@time: 10/09/2017 19:49 
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows == 3:
            return [[1],[1,1],[1,2,1]]
        else:
            Base = [[1], [1,1],[1,2,1]]
            for i in range(3,numRows):
                currRow = [1]
                for j in range(0, i-1):
                    currValue = Base[i-1][j] + Base[i-1][j+1]
                    currRow.append(currValue)
                currRow.append(1)
                #print currRow
                Base.append(currRow)
                #print Base
            return Base
