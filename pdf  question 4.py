# 4. Write a Python program to reverse a string.Sample String : "1234abcd"
def reverse(x):
    i=0
    while i<len(x):
        i+=1
    print(x[::-1])
a="1234abcd"
reverse(a)