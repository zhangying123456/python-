



import random

def fn(x):
    return x**2

result = []
for i in range(3):
    t = random.randint(1, 10)
    print (t)
    r = fn(t)
    result.append(r)
print (result)


value = eval(input())
print(value)
