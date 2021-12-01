# 3. Write a Python function to multiply all the numbers in a list. Sample List : (8, 2,3, -1, 7)


def multi(x):
    i=0
    total=1
    while i<len(x):
        total=total*x[i]
        i+=1
    print(total)
a=[8,2,3,-1,7]
multi(a)
