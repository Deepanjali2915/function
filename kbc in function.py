def question():
    question = [
    "How many continents are there?", # pehla question
    "What is the capital of India?", # doosra question
    "NG mei kaun se course padhaya jaata hai?" # teesra question
    ]
    return question 
question_list=question()
def option():       
    option = [
    #pehle question ke liye options
    ["1.Four", "2.Nine", "3.Seven", "4.Eight"],
    #second question ke liye options
    ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
    #third question ke liye options
    ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
    ]
    return option
options_list=option()    
def sol():    
    # har ek question ke liye, uski solution key (yeh index nahi hai)
    sol = [3, 4, 1]
    return sol 
solution_list=sol() 

i=0
a=0
b=1
count=0
prize=0
while i<len(question_list):
    print(question_list[i])
    j=0
    ans=["3 seven", "4 eight","4 delhi","1 Chandigarh","1 Software Engineering","2 Counseling"]
    print(options_list[i])
    if count<1:
        user=input("Do you want lifeline \ny/n")
        if user=="y":
            print("you have only one time use 50-50life line:  ")
            print(ans[a+i])
            print(ans[b+i])
            answer=int(input("enter the answer: "))
            if answer==solution_list[i]:
                print("your answer is right,\n")
                prize+=10000
                print("Apka prize ha ",prize,"\n")
            else:
                print("your ans is wrong\n")
                break
                
            count+=1
        elif user=="n":
            answer=int(input("enter the answer: "))
            if answer==solution_list[i]:
                print("your ans is right,\n")
                prize+=10000
                print("Apka prize ha",prize,"\n")
            else:
                print("your ans is wrong\n")
                break
                
    else:
        print("sorry! but your life line is finished\n")  
        answer=int(input("enter the answer: "))
        if answer==solution_list[i]:
            print("your ans is right,\n")
            print("You are the winner\n")
            prize+=10000
            print("Apka prize ha",prize,"\n")
        else:
            print("your ans is wrong\n")
            break
         
    i+=1       
    a+=1
    b+=1
print("Your total prize is: ", prize)
