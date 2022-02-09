'''
Author: BDFD
Date: 2021-11-15 13:50:55
LastEditTime: 2021-12-18 19:53:17
LastEditors: BDFD
Description: 
FilePath: \code\10.循环嵌套.py
'''
# 在控制台中打印如下图形
# *****
# *****
# *****
# *****
# *****
# 

# 创建一个循环来控制图形的高度
# 循环嵌套时，外层循环没执行一次，内存循环就要执行一圈
# i = 0
# while i < 5:
#     # 创建一个内层循环来控制图形的宽度
#     j = 0
#     while j < 5:
#         print("* ",end='')
#         j += 1
#     print()
#     i += 1

#
# *     j<1   i=0
# **    j<2   i=1   
# ***   j<3   i=2
# ****  j<4   i=3
# ***** j<5   i=4
# 
# ***** j=5 i=1
# ****  j=4 i=2
# ***   j=3 i=3
# **    j=2 i=4
# *     j=1 i=5

i = 0
num =5
while i < num:
    j = 0
    while j < num-i:
        print("* ",end='')
        j += 1
    print()
    i += 1

