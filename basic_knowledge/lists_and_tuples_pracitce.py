# -*- coding : utf-8-*-
"""
Lists and Tuples
"""

# 已知一个列表中有某些元素重复，编程去掉重复元素，形成一个新列表
messy_list = [1, 2, 2, 3, 3, 4, 4, 5, 6, 10, 9, 6]
new_list = []
for i in messy_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# 对其进行升序和降序
new_list.sort()
print('升序后为', new_list)
new_list.sort(reverse=True)
print('降序后为', new_list)

"""
已知斐波那契数列的前两个数据为 0 和 1，计算其前 10 项。
斐波那契数列:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""

fib_list = [0, 1]
for i in range(2, 10):
    fib_list.append(fib_list[-1] + fib_list[-2])
print(fib_list)
