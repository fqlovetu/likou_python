# -*- coding: utf-8  -*-
# ！/usr/bin/env python
# @Time :2020/7/7 15:39 
# @Author :Sheng Chen
# @Email :sheng.chen@inossem.com
import sys

sys.path.append(r'/home/chensheng/likou')
from typing import List, Tuple


class Solution:
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]
    fillIndex = []
    isValid = False
    ini = False

    def isValidSudoku(self, board: List[List[str]]):
        # global rows,columns,boxes,fillIndex,isValid
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    self.rows[i][num] = self.rows[i].get(num, 0) + 1
                    self.columns[j][num] = self.columns[j].get(num, 0) + 1
                    boxIndex = (i // 3) * 3 + j // 3
                    self.boxes[boxIndex][num] = self.boxes[boxIndex].get(num, 0) + 1
                    if self.rows[i][num] > 1 or self.columns[j][num] > 1 or self.boxes[boxIndex][num] > 1:
                        return
                else:
                    self.fillIndex.append((i, j))
        self.isValid = True
        self.ini = True

    def solveSudoku(self, board: List[List[str]]) -> None:
        if not self.ini:
            self.isValidSudoku(board)
        if not self.isValid:
            return
        if len(self.fillIndex) == 0:
            return True
        i, j = self.fillIndex.pop(0)
        row = self.rows[i]
        column = self.columns[j]
        box = self.boxes[(i // 3) * 3 + j // 3]
        dic = {**row, **column, **box}
        candidate_num = [str(num) for num in range(1, 10) if str(num) not in dic]
        if len(candidate_num) == 0:
            self.fillIndex.insert(0, (i, j))
            return False
        else:
            for num in candidate_num:
                board[i][j] = num
                self.rows[i][num] = 1
                self.columns[j][num] = 1
                self.boxes[(i // 3) * 3 + j // 3][num] = 1
                a = self.solveSudoku(board)
                if not a:
                    board[i][j] = '.'
                    del self.rows[i][num]
                    del self.columns[j][num]
                    del self.boxes[(i // 3) * 3 + j // 3][num]
                else:
                    return True
            self.fillIndex.insert(0, (i, j))
            return False


if __name__ == '__main__':
    board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    obj = Solution()
    obj.solveSudoku(board)
    print(board)
    print(4//2*2)
