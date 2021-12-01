
def calculator(number_x, number_y, operation):
    print(number_x*number_y)
    if operation=="sum":
        print(number_x+number_y)
        # return number_x+number_y
    elif operation=="Subtract":
        print(number_x-number_y)
        # return number_x-number_y
    elif operation=="multiply":
        print(number_x*number_y)
        # return number_x*number_y
    elif operation=="Devide":
        print(number_x//number_y)
        # return number_x//number_y
a=int(input("enter the number"))
b=int(input("enter the number"))
add_result=calculator(a,b,"sum")
subtract_result=calculator(a,b,"Subtract")
multiply_result=calculator(a,b,"multiply")
divide_result=calculator(a,b,"Devide")



# # number_1=calculator(24,20,"sum")
# # number_2=calculator(50,60,"Subtract")
# # number_3=calculator(80,120,"multiply")
# # number_4=calculator(90,23,"Devide")
# # print(number_1)
# # print(number_2) 
# # print(number_3)                       
# # print(number_4)

# list_change=([5, 10, 50, 20], [2, 20, 3, 5])    
# number_x=0
# while number_x<len(list_change):
#     number_y=0
#     while number_y<len(list_change[number_x]):
#         number_y+=1
#     number_x+=1        
#     print(list_change[number_x]*list_change[number_x][number_y])
#     calculator(i,j,"multiply")  




list_change=([5, 10, 50, 20], [2, 20, 3, 5])
i=0
while i<len(list_change):
    j=0
    while j<len(list_change[i]):
        # calculator(list_change[i],list_change[i][j])
        j+=1
    i+=1    
calculator(list_change[i],list_change[i][j])    