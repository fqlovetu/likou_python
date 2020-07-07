# -*- coding: utf-8  -*-
# ！/usr/bin/env python
# @Time :2020/7/7 15:27 
# @Author :Sheng Chen
# @Email :sheng.chen@inossem.com
import sys

sys.path.append(r'/home/chensheng/likou')
from typing import List
class Solution:
    def isValidSudoku(self,board:List[List[int]])->bool:
        rows=[{} for i in range(9)]
        columns=[{} for i in range(9)]
        boxes=[{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num!='.':
                    num=int(num)
                    rows[i][num]=rows[i].get(num,0)+1
                    columns[j][num]=columns[j].get(num,0)+1
                    boxes_index=(i//3)*3+j//3
                    boxes[boxes_index][num]=boxes[boxes_index].get(num,0)+1
                    if rows[i][num]>1 or columns[j][num]>1 or boxes[boxes_index][num]>1:
                        return False
        return True
if __name__ == '__main__':
    dic1={}
    dic1['a']=dic1.get('a',0)+1
    print(dic1)