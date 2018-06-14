print("hello world")

str='5'+'8'
print(str)

str1='C:\\now'
print(str1)

str2=r'C:\Users\zhangying1\Desktop\全局搜索\信息中心\测试文档\测试报告\客户端'
print(str2)
str3='C:\\Users\\zhangying1\\Desktop\\全局搜索\\信息中心\\测试文档\\测试报告\\客户端'
print(str3)

str4='哈哈,\n哈哈哈哈,\n哈哈哈...'
print(str4)
str5='''哈哈，
哈哈哈哈，
哈哈哈哈哈，
哈哈哈哈，
哈哈...'''
print(str5)

#单引号
str1='python'
#单引号中使用双引号
str2='"python"'
#双引号中使用单引号
str3="'python'"
#三单引号
str4='''python'''
#三单引号中间使用双引号
str5='''"python"'''
#三单引号中有换行符
str6='''hello
python'''
#三双引号中有换行符
str7="""hello
python"""

print("str1: {}".format(str1))
print("str2: {0}".format(str2))
print("str3: {0}".format(str3))
print("str4: {0}".format(str4))
print("str5: {0}".format(str5))
print("str6: {0}".format(str6))
print("str7: {0}".format(str6))