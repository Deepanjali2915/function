# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter 
# lega aur 0 se limit tak ke beech ke sabhi even aur odd numbers ko label ke saath print 
# karega jaisa ki niche dikhaya gaya hai.

# def shownumbers(x,num):
#     i=0
#     while i<=num:
#         if i%2==0:
#             print(i,"even")
#         else:
#             print(i,"odd")
#         i+=1
# a=int(input("enter the nuumber:"))
# shownumbers(0,a)



Original=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=Original[0]
count=0
while i<len(Original):
    if Original[i]<max:
        max=Original[i]
        count+=1
    i+=1
print(count,max)        