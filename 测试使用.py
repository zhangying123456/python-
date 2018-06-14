import random
import linecache

# print("who do you think I am?")
# input()
# print("yes")

# name = 'zhang'
# print(name)
# name = 'ying'
# print(name)
#
# value = 3*4
# print(value)
# value = 2<5
# print(value)
#
# # name = input()
# # print(name)
#
# a = 1 < 3
# print(a)
# print(not a)
# b = 1
# c = 3
# print (not b != c)

#while循环
# num = randint(1,3)
# print("Guess what I think")
# bingo = False
#
# while bingo == False:
#     answer = int(input())
#     if answer < num:
#         print("too small")
#     if answer > num:
#         print("too big")
#     else:
#         print("equal")
#         bingo = True

# i = 1
# s=0
#
# while (i<=100):
#     s+=i;
#     i+=1;
# print(s)

#for循环
# for i in range(1, 11):
#     print(i)

#字符串
# print("It's good")
# print("good")
# print('good')
# print('women "zai"')
# print('I\'am a \"good\" teacher')
# print("this is the\
# same line")
# print('''
# "What's your name?" I asked.
# "I'm Han Meimei."
# ''')
#
# print('He said,\"I\'am yours!\"')
# print('\\\\_v_//')
#
# print('''
# Stay hungry,
# stay foolish.
#             -- Steve Jobs''')
#
# print("""
# *
# ***
# *****
# ***
# *
# """)

# #字符串的格式化
# str1 = "good"
# str2 = "bye"
# print(str1+str2)
# print(str1+"very"+str2)
#
# num =18
# print('my age is'+str(num))

#循环的嵌套
# for i in range(0,5):
#     print('*',end=' ')

# print('a', end=' ')
# print('a', end='1234')

# for i in range(0, 5):
#     for j in range(0, i+1):
#         print('*',end=' ')
#     print()

# #字符创的格式化
# #Python中bool除了''、""、0、()、[]、{}、None为False之外，其他的都是True
# print(bool('False'))
# print(bool('abc'))
# print(bool(-123))
# print(bool(''))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))
# print(bool(None))

#函数
#定义一个函数
# def sayhello():
#     print("helloword")
#
# sayhello()

# def isEqual(num1, num2):
#    if num1<num2:
#        print ('too small')
#        return False;
#    elif num1>num2:
#        print ('too big')
#        return False;
#    else:
#        print ('bingo')
#        return True
#
# from random import randint
# num = randint(1, 100)
# print ('Guess what I think?')
# bingo = False
#
# while bingo == False:
#    answer = int(input())
#    bingo = isEqual(answer, num)


# l = [1, 1, 2, 3, 5, 8, 13]
# print(l)
#
# l[0]='ad'
# print(l)
#
# l.append(100)
# print(l)
#
# del l[2]
# print(l)
#
# print(l[1])
# print(l[-1])
# print(l[-3])
# print(l[1:3])
# print(l[:4])
# print(l[3:])
# print(l[:])
# print(l[1:-1])


# print(choice('a string'))

# #字符串分割
# string = 'i want to travel all the word'
# print(string.split())
#
# st0= 'iisongiiihuaniiiigongi'
# print(st0.split('i',3))
# print(st0.split('i',3)[2])
#
# u = "www.doiido.com.cn"
# print(u.split())
# print(u.split('.'))
# print(u.split('.',0))
# print(u.split('.',1))
# print(u.split('.',2))
# print(u.split('.',2)[1])
#
# u1,u2,u3=u.split('.',2)
# print(u1)
# print(type(u1))



# 连接
# print(','.join(['apple','love','you']))
# print(','.join('helloword'))



# word = 'helloword'
# for c in word:
#     print(c,end=' ')
#
# print(word[1])
# print(word[-1])


# #默认读取所有内容
# file = open('hhh.txt')
# data = file.read()
# print(data,end='')
# print(type(data))
# file.close()
#
# #读取部分数据
# file1 = open('hhh.txt')
# data1 = file1.read(7)
# print(data1)
# print(type(data1))
# file1.close()
#
# #每次读取一行数据
# #逐行读取文件内容
# file2 = open('hhh.txt')
# #file2 = open(r'C:\Users\zhangying1\PycharmProjects\test1\hhh.txt')  路径前面加上r避免转义
# data2 = file2.readline()
# while data2:
#     print(data2,end='')
#     data2 = file2.readline()
# file2.close()
#
# #读取文件所有行
# file3 = open('hhh.txt')
# data3 = file3.readlines()
# print(type(data3))
# print(data3)
# for line in data3:
#     print(line.strip())  #strip() 把末尾的'\n'删掉
# file3.close()
#
# #输入某个特定行
# text = linecache.getline('hhh.txt',1)
# print(text)


# #写文件
# file = open('hhh.txt','w')
# file.write('run run')
# file.close()
#
# file1 = open('hhh.txt','a')
# file1.write(' '+'keeping study')
# file.close()

# open('output.txt','w').write(open('hhh.txt').read())


# file = open('output.txt','w')
# file.write(input())
# file.close()


# f = open('scores.txt',encoding='utf-8')
# #用readlines，把每一行分开，便于之后的数据处理
# lines = f.readlines()
# print(lines)
# f.close()
# results = []
#
# #data[0]是姓名，data[1:]是所有成绩组成的列表
# #每次循环中，sum都要先清零
# #score是一个字符串，为了做计算，需要转成整数值int
# #results需要在循环之前初始化results = []
# for line in lines:
#     data = line.split()
#     sum = 0
#     for score in data[1:]:
#         sum += int(score)
#     result ='%s\t:%d\n'%(data[0], sum)
#     results.append(result)
# print(results)
# output = open('result.txt', 'w',encoding='utf-8')
# output.writelines(results)
# output.close()

# #break、continue
# sum=0
# for score in [61,52,63,4]:
#    point = int(score)
#    if point < 60:
#        break
#    sum += point
# print(sum)

# #异常处理
# try:
#     file=open('haha.txt')
#     print('file oened')
#     file.close()
# except:
#     print('file not exists')
# print('done')


# score = {'萧峰': 95,'段誉': 97,'虚竹': 89}
# print(score['段誉'])
# for name in score:
#     print(name)
# score['虚竹']=100
# print(score)
# score['慕容复']=60
# print(score)
# del score['萧峰']
# print(score)
# score.clear()
# print(score)
#
# #创建新的字典
# d={}
# d['women']='hello'
# print(d)

# #random.random()用于生成一个0到1的随机浮点数数: 0 <= n < 1.0
# print(random.random())
#
# #random.uniform(a, b)，用于生成一个指定范围内的随机浮点数
# print(random.uniform(30,20))
#
# #random.randint(a, b)，用于生成一个指定范围内的整数
# print(random.randint(30,50))
#
# #random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数
# print(random.randrange(10,100,10))
#
# #random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence
# print(random.choice('women很好'))
# print(random.choice(['hhh','wo',12]))
# print(random.choice(('wolf','elephant','penguin')))
#
# #random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列
# p = ["Python", "is", "powerful", "simple", "and so on..."]
# print(random.sample(p,5))
# print(p)
#
# #random.shuffle() 是用来打乱列表元素的，没有返回值
# p1=[1,2,3,4,5]
# random.shuffle(p1)
# print(p1)


# l=[2,3,4,7]
# for i in range(len(l)):
#     print(i,l[i])

#将一个字符串反转并输出
# s='python'
# print(s[::-1])

#将一个字符串反转并输出
l=list('python')
print(type(l))
l.reverse()
print(','.join(l))
