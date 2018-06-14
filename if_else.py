temp=input("请输入1到100之间的数字：")
num=int(temp)
if 1<=num<=100:
    print('好漂亮')
else:
    print('不好看')

print(".............woaini..................")
temp = input("猜猜是哪个数：")
guess = int(temp)
if guess == 8:
    print("对啦")
else:
    if guess > 8:
        print("大啦")
    else:
        print("小啦")
print("游戏结束")
