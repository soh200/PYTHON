a=int(input())
b=int(input())
c=int(input())
if( a>=b and a<=c):
    print(a," is the median")
elif( b>=a and b<=c):
    print(b," is the median")
else:
    print(c," is the median")
