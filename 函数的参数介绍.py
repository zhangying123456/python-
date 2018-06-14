# #位置参数
# def power(x):
#     return x*x
# print(power(5))
#
#
# def power(x,n):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# print(power(5,4))
#
# #默认参数
# def power(x,n=2):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# print(power(5))
#
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
# enroll('zhang','F')
# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', city='Tianjin')



# def add_end(L=[]):
#     L.append('END')
#     print(L)
# add_end()
# add_end()


# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     print(L)
# add_end()
# add_end()

def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    print(sum)
calc([1,5,3])





