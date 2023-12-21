""" amstrong no :
153 = 1*1 + 5*5 + 3*3 = 153
sum of square of digits.
n=153
res= 153%10 = 3
sum += res* res
n = 153/10
important to store otherwise it shows false

"""

n = int(input())
m =  n  
sum = 0
while(n!=0):
    res = n%10
    sum += int(res*res*res)
    n = int(n/10)
    
if(sum == m):
    print("yes")
else:
    print("No")
    

