'''
Author: BDFD
Date: 2021-11-15 13:50:55
LastEditTime: 2021-12-18 20:26:40
LastEditors: BDFD
Description: 
FilePath: \code\13.break和continue.py
'''
# break
# break可以用来立即退出循环语句（包括else）
# continue
# continue可以用来跳过当次循环
# break和continue都是只对离他最近的循环起作用
# pass
# pass是用来在判断或循环语句中占位的

# 创建一个5次的循环
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# else :
#     print('循环结束')

# i = 0
# while i < 5:
#     i += 1
#     if i == 2:
#         continue
#     print(i)
# else :
#     print('循环结束')

i = 0
if i < 5:
    pass