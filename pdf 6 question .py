# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].


def even(x):
    a=[]
    i=0
    while i<=len(x):
        if i%2==0:
            a.append(i)
        i+=1    
            # print(a)
    return a
print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
