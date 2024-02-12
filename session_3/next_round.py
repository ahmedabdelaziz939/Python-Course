n,k=map(int,input().split())
x=list(map(int,input().split()))
num=0
for score in x:
    if score >= x[k-1] and score>0:
        num+=1
print(num)