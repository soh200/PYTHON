print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
a=input("enter the month ");
if a=="February":
    print("no of days: 28days ")
elif a in ("April", "June", "September", "November"):
    print("no of days: 30days ")
elif a in("January", "March", "May", "July", "August", "October", "December"):
    print("no of days: 31days ")
else :
    print("Wrong input ");
    
