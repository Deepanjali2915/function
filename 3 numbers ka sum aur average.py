# Question 3
#     Ek function banaiye jo 3 numbers ka sum aur average print kare.Hum user se 3 number input
#      karwayenge aur fir unn 3 numbers ka sum aur average print karwayenge jaisa ki niche output 
#      diya hua hain.
# Input:-
# enter first number :-3
# Enter second number :-4
# Enter third number:-5    
def num(a,b,c):
    sum=a+b+c
    Average=sum//3
    print("sum of 3 numbers",sum)
    print("Average of 3 numbers",Average)
x=int(input("enter the number: "))
y=int(input("Enter the number: "))
z=int(input("enter the number: "))
num(x,y,z)    