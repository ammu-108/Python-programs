n = int(input())
res = []
if n ==0:
    print(res)
elif n==1:
    print(res[0,1])
elif n >= 2:
    res=[0,1]
    for i in range(2 ,n+1):
        res.append(res[i-1] + res[i-2])
        
print(res)
        
