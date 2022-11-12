# -*- coding : utf-8-*-
"""list example"""

# 列表 list
list_4 = [5, 'a', 2.3]
list_any = [1, 2, 3, 'foo', 'bar', (1, 2, 3), {'A': 'a', 'B': 2}]
#           数值型    字符串        元组         字典（json)
print(list_any)
print('list_any的第一位值', list_any[0])
print('list的最后一位', list_any[-1])
print('list_4 + list_any', list_4 + list_any)

# 遍历组装list
# L = ['foo']
# for i in range(10):
#     # 0-9
#     L.append(i)
# print(L)

# 遍历取出list中元素
# # _i 下划线变量代表私有
# for _i in L:
#     print(_i)

# list_extend = [[1, 2, 3], ['foo', 'bar'], [6, 8, 9]]
# for l in list_extend:
#     L.extend(l)
# print(L)

# list排序
# reverse = True 降序， reverse = False 升序
# l = [9, 2, 3, 4, 5]
# l.sort(reverse=True)
# print('降序', l)
# l.sort(reverse=False)
# print('升序', l)
