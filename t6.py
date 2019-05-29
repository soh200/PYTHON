a=int(input())
b=int(input())
c=int(input())
if ((a+b)<=c) or ((a+c)<=b) or ((b+c)<=a):
    print("not a triangle")
elif a==b and a==c:
    print("equileteral triangle ")
elif (a==b) or (a==c) or (b==c):
    print("isosceles triangle ");
elif ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("scalene triangle ")
else:
    print("not a triangle");

