n = int(input())
cn = 1
while(cn <=n ):
    if cn% 3 == 0:
        print("Fizz")
    elif cn%5 == 0:
        print("Buzz")
    elif cn%3==0 and cn%5==0:
        print("FizzBuzz")
    else:
        print(cn)
        
    cn= cn+1

