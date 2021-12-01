# Question (Part 1)

# check_numbers naam ka ek function likhiye jo do numbers le aur fir print 
# kare "Dono even hain" agar dono numbers even (2 se divide hote hain) nahi
#  toh print kare "Dono numbers even nahi hai"
def check_number(x,y):
    if x%2==0 and y%2==0:
        print("Dono even ha")
    else:
        print("Dono numbers even nahi ha")
# check_number(12,68)            



# Question (Part 2)
# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko
#  arguments ki tarah le aur fir check kare ki same index waale dono integers even hain ya nahi.
# Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo.
# Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] Toh usko yeh 
# output deni chaiye:
# dono even hain
# dono even nahi hai
# dono even hain
# dono even hain
# dono even nahi hain
# dono even nahi hain
a=[2, 6, 18, 10, 3, 75]
b=[6, 19, 24, 12, 3, 87]
i=0
while i<len(a):   
    check_number(a[i],b[i])
    i+=1

# i=0
# while i<len(a):
#     # if a[i]%2==0 and b[i]%2==0:
#     #     print("dono enen ha")
#     # else:
#     #     print("Dono even nahi ha")
#     check_numbers(a[i],b[i])
#     i+=1