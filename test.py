# def num(x):
#     i=0
#     while i<=x:
#         if i%2==0:
#             print("even no.",i)
#         else:
#             print("odd no.",i)
#         i+=1    
# num(30)                



# def num(x,y,z):
#     if x>y and x>z:
#         print("x is big",x)
#     elif y>x and y>z:
#         print("y is big",y)
#     else:  
#         print("z is big",z) 
# a=int(input("num"))
# b=int(input("num"))            
# c=int(input("num"))
# num(a,b,c)


# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].


def sample(x):
    a=[]
    sum=0
    for i in x:
        if i not in a:
            a.append(i)
            sum=sum+i
    print(sum)        
    return a

print(sample([1,2,3,3,3,3,4,5]))            