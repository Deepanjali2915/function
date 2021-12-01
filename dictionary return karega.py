# Question 8
# Ek function likho jo ki ek argument le jo number ho or dictionary
#  return karega jisme keys 1 se lekar argument ke number tak hogi aur values unke 
#  squares honge.jaisa ki niche dikhaya gaya hai.
def num(a):
    i=0
    d={}
    while i<=a:
        d[i]=i*i
        print(d)
        i+=1
num(20)        


