import math
n,m,a=map(int,input().split())
x=math.ceil(n/a)
y=math.ceil(m/a)
result=x*y
print(result)