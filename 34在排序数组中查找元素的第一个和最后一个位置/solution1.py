# -*- coding: utf-8  -*-
# ！/usr/bin/env python
# @Time :2020/7/7 14:12 
# @Author :Sheng Chen
# @Email :sheng.chen@inossem.com
import sys

sys.path.append(r'/home/chensheng/likou')

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def searchRange(self,nums:List[int],target:int)->List[int]:
        #需要考虑重复元素
        lens=len(nums)
        if lens==0:
            return [-1,-1]
        start=0
        end=lens-1
        indexList=[]
        while start<=end:
            mid=start+(end-start)//2
            if  nums[mid]==target:
                index1=mid-1
                while start<=index1 and nums[index1]==target  :
                    indexList.append(index1)
                    index1-=1
                indexList.append(mid)
                index2=mid+1
                while index2<=end and nums[index2]==target  :
                    indexList.append(index2)
                    index2+=1
                indexList.sort()
                return [indexList[0],indexList[-1]]
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return [-1,-1]
if __name__ == '__main__':
    obj=Solution()
    print(obj.searchRange([1,2,3,3,3,3,4,5,9,3],3))





