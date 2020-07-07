# -*- coding: utf-8  -*-
# ！/usr/bin/env python
# @Time :2020/7/7 14:42 
# @Author :Sheng Chen
# @Email :sheng.chen@inossem.com
import sys

sys.path.append(r'/home/chensheng/likou')
from typing import List

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# #
# # 你可以假设数组中无重复元素。
class Solution:
    def searchInsert(self,nums:List[int],target:int)->int:
        lens=len(nums)
        if lens==0:
            return 0
        start=0
        end=lens-1
        while start<=end:
            mid=start+(end-start)//2#若为2个元素，mid取第一个元素
            if nums[mid] == target:
                return mid  # 无重复元素
            if nums[mid]<=nums[end]:#升序
                if target<nums[mid]:
                    if nums[start]==target:
                        return start
                    elif nums[start]<target:
                        end=mid-1
                    else:
                        return start
                else:
                    if nums[end] == target:
                        return end
                    elif nums[end] > target:
                        start = mid + 1
                    else:
                        return end + 1
            else:#降序
                if target > nums[mid]:
                    if nums[start] == target:
                        return start
                    elif nums[start] > target:
                        end = mid - 1
                    else:
                        return start
                else:
                    if nums[end] == target:
                        return end
                    elif nums[end] < target:
                        start = mid + 1
                    else:
                        return end + 1
if __name__ == '__main__':
    obj=Solution()
    print(obj.searchInsert([1,3,5,6],5))
    print(obj.searchInsert([1, 3, 5, 6], 2))
    print(obj.searchInsert([1, 3, 5, 6], 7))
    print(obj.searchInsert([1, 3, 5, 6], 0))
    print(obj.searchInsert([1, 3], 2))

