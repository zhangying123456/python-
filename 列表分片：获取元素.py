mem=['我','们','在','这']
#前面数字表示开始member[1]，后面数字不包含，表示数据到member[i-1]
print(mem[:2])


list7=[3,6,8,1,0,4,9]
list8=list7
list9=list7[:]
list7.sort()
print(list7)
print(list8)
print(list9)