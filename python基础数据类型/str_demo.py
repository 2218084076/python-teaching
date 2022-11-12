"""demo"""
# 变量
# 变量命名
# 正确：
#     _i ,_name,__value (以下划线开头)
#     Captcha (以大写字母开头)
#     abc  （以小写字母开头）

# 字符串拼接
# test = 'abc' + 'b'
# print(test)
# test_2 = f'{test},qws'
# print(test_2)
# test_3 = 'a=%s b=%s' % (1, 2)
# # print(test_3)
# list_a = ['foo', 'bar', '1', '3']
# print('|'.join(list_a))
# print(len(''.join(list_a)))
# print(len(list_a))

# 列表 list
# list_4 = [5, 'a', 2.3]
# list_any = [1, 2, 3, 'foo', 'bar', (1, 2, 3), {'A': 'a', 'B': 2}]
# #           数值型    字符串        元组         字典（json)
# print(list_any)
# print('list_any的第一位值', list_any[0])
# print('list的最后一位', list_any[-1])
# print('list_4 + list_any', list_4 + list_any)

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

# 字典
# d = {key1 : value1, key2 : value2 }
# d = {'key1': 'value1', 'key2': 2}
# 取值
# print(d['key1'])
# print(d.get('q', 0))  # get方法取值,当key不存在,不会抛出异常,则返回默认值
# print(d.get('key1'))
# d['key1'] = 1  # 更新字典
# print(d)
# d['a'] = 'a'  # 添加键值对
# print(d)
# print('所有key', d.keys())
# print('所有value', d.values())

# set集合 单一元素，可以加减
# list_5 = [1, 2, 3, 3, 3, 4]
# print(set(list_5))

# l = [1, 2, 3, 4]
# t = (1, 2, 3, 4)
# print('to tuple', tuple(l))
# print('to list', list(t))

# k = ['a', 'b']
# v = [1, 3]
# print('list to dict', dict(zip(k, v)))


