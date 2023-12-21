"""
 if no is div by 400 OR div by 4 but not 100 is called leap year.   
  which satisfies either if one condition it is leap year.  
    
"""


n = int(input())
if n%400==0 or ( n%4 ==0 and  n%100!=0 ):
    print("leap year")
else:
    print("non leap")

