# 2. Write a Python function to sum all the numbers in a list. Sample List : (8, 2, 3,0, 7)

def sum(x):
    i=0
    sum=0
    while i<len(x):
        sum+=x[i]
        i+=1
    print(sum)
x=[8,2,3,0,7]
sum(x)        

