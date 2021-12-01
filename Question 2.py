# def printline(name,post):
#     print(name)
#     print(post)
# printline("Mera naam nayak ha","or mai pune coumpus ki girls ko padataa hu")    



# a=[]
# size=int(input("Enter the number:"))
# for i in range(size):
#     value=int(input("enter the number"))
#     a.append(value)
# min=a[0]
# i=0
# while i<len(a)-1:
#     j=0
#     while j<len(a)-1:
#         if a[i]<a[i+1]:
#             c=a[i]
#             a[i]=a[i+1]
#             a[i+1]=c
#             min<a[i]
#             min.append(a[i])
#             i+=1
#         j+=1
# print(min)            
list_change=([5, 10, 50, 20],[2, 20, 3, 5])
i=0
b=[]
while i<len(list_change):
        c=list_change*list_change[i]
        b.append(c)
        i+=1    
print(b)
