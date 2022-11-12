"""demo"""
# 变量
# 变量命名
# 正确：
#     _i ,_name,__value (以下划线开头)
#     Captcha (以大写字母开头)
#     abc  （以小写字母开头）


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

# 类型之间相互转化
# l = [1, 2, 3, 4]
# t = (1, 2, 3, 4)
# print('to tuple', tuple(l))
# print('to list', list(t))

# k = ['a', 'b']
# v = [1, 3]
# print('list to dict', dict(zip(k, v)))
