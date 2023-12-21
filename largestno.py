n = list(map(int,input().split()))
maxi = n[0]
for i in n:
    if i > maxi:
        maxi = i

print(maxi)

