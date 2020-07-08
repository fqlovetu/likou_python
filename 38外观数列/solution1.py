# -*- coding: utf-8  -*-
# ！/usr/bin/env python
# @Time :2020/7/8 9:44 
# @Author :Sheng Chen
# @Email :sheng.chen@inossem.com
import sys

sys.path.append(r'/home/chensheng/likou')
from typing import List
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
#
# 注意：整数序列中的每一项将表示为一个字符串。
#
# # 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1
#
# 描述前一项，这个数是 1 即 “一个 1 ”，记作 11
#
# 描述前一项，这个数是 11 即 “两个 1 ” ，记作 21
#
# 描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211
#
# 描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-and-say
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def countAndSay(self,n:int)->str:
        str_1='1'
        for i in range(n-1):
            str_2=''
            char_pre=str_1[0]
            count=1
            for j in range(1,len(str_1)):
                char_now=str_1[j]
                if char_now==char_pre:
                    count+=1
                else:
                    str_2+=str(count)+char_pre
                    count=1
                    char_pre=char_now
            str_2+=str(count)+char_pre
            str_1=str_2
        return str_1
if __name__ == '__main__':
    obj=Solution()
    print(obj.countAndSay(4))



