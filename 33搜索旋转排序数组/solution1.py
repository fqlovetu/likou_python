# -*- coding: utf-8  -*-
# ！/usr/bin/env python
# @Time :2020/7/7 12:21 
# @Author :Sheng Chen
# @Email :sheng.chen@inossem.com
import sys
sys.path.append(r'/home/chensheng/likou')
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
class Solution():
    def search(self,nums:List[int],target:int)->int:
        lens=len(nums)
        if lens==0:
            return -1
        start=0
        end=lens-1
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[start]:#左部分升序
                if nums[start]<=target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                #右部分升序
                if nums[mid]<target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1
if __name__ == '__main__':
    obj=Solution()
    a=obj.search([3,1],1)
    print(a)
