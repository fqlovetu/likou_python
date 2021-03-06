# -*- coding: utf-8  -*-
# ！/usr/bin/env python
# @Time :2020/7/7 15:06 
# @Author :Sheng Chen
# @Email :sheng.chen@inossem.com
import sys

sys.path.append(r'/home/chensheng/likou')
from typing import List
class Solution:
    def isValidSudoku(self,board:List[List[str]])->bool:
        import numpy as np
        array=np.array(board)
        for i in range(9):
            row=array[i]
            row=[num for num in row  if num!='.']
            if len(row)!=len(set(row)):
                return False
        for i in range(9):
            column=array[:,i]
            column=[num for num in column if num!='.']
            if len(column)!=len(set(column)):
                return False
        for i in range(3):
            for j in range(3):
                array_temp=array[i*3:i*3+3,j*3:j*3+3]
                list_temp=[num for num in array_temp.flat if num!='.']
                if len(list_temp)!=len(set(list_temp)):
                    return False
        return True


if __name__ == '__main__':
    obj=Solution()
    list=[["5","3","0","2","7","6","4","1","8"],["6","2","4","1","9","5","3","0","7"],["1","9","8","3","4","0","5","6","2"],["8","1","2","7","6","4","0","5","3"],["4","0","6","8","5","3","7","2","1"],["7","5","3","0","2","1","8","4","6"],["0","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","6","8","2","1","7","9"]]
    print(obj.isValidSudoku(list))
    list2=[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    print(obj.isValidSudoku(list2))