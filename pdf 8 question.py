# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and
# lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def case():
    x='The quick Brown Fox'
    i=0
    count=0;count1=0;count2=0
    for i in x:
        if i.isupper():
            count+=1
        elif i.islower():
            count1+=1
        else:
            count2+=1  
        
    print("No. of Uppercase characters :",count)
    print("No. of Lowercase Characters :",count1)
    print("No. of space in characters ",count2)
case()

