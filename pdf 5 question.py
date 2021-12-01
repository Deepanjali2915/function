# Q5.Write a Python function that takes a list and returns a new list with unique 
# elements of thefirst list.
# first list.
# Unique List : [1, 2, 3, 4, 5].
# Sample List : [1,2,3,3,3,3,4,5]
def unique(x):
    a=[]
    for i in x:
        if i not in a:
            a.append(i)
    return a
print(unique([1,2,3,3,3,3,4,5]))