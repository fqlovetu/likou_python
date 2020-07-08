# -*- coding: utf-8  -*-
# ！/usr/bin/env python
# @Time :2020/7/7 15:27 
# @Author :Sheng Chen
# @Email :sheng.chen@inossem.com
import sys

sys.path.append(r'/home/chensheng/likou')
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[int]]) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes_index = (i // 3) * 3 + j // 3
                    boxes[boxes_index][num] = boxes[boxes_index].get(num, 0) + 1
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[boxes_index][num] > 1:
                        return False
        return True


if __name__ == '__main__':
    obj = Solution()
    list1 = [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
    print(obj.isValidSudoku(list1))
    list2 = [["5", "3", "0", "2", "7", "6", "4", "1", "8"], ["6", "2", "4", "1", "9", "5", "3", "0", "7"],
             ["1", "9", "8", "3", "4", "0", "5", "6", "2"], ["8", "1", "2", "7", "6", "4", "0", "5", "3"],
             ["4", "0", "6", "8", "5", "3", "7", "2", "1"], ["7", "5", "3", "0", "2", "1", "8", "4", "6"],
             ["0", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
             ["3", "4", "5", "6", "8", "2", "1", "7", "9"]]
    print(obj.isValidSudoku(list2))
