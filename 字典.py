dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#删除键是'Name'的条目
del dict['Name']
print(dict)

#清空词典所有条目
dict.clear()
print(dict)

#删除词典
del dict
print(dict)

#修改键/值
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8
print(dict)

#增加新的键/值
dict['School'] = "DPS School"
print(dict)