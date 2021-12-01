# 1. Write a Python function to find the Max of three numbers.


def max(a,b,c):
    if b<a and b>c:
        print("a is greater",a)
    elif a<b and b>c:
        print("b is greater",b)
    else:
        print("c is greater",c)
x=int(input("Enter the number:"))
y=int(input("Enter the number:")) 
z=int(input("Enter the number:"))              
max(x,y,z) 