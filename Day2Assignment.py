#Assignment 1
#Marksheet
marks = int(input("Enter your grade: "))
if (marks<=100) and (marks>=90):
    print("Grade is A+")
elif (marks <90 and marks>=75):
    print("Grade is A")
elif (marks<75 and marks>=60):
    print("Grade is B+")
elif (marks<60 and marks >=50):
    printf("Grade is B")
elif (marks<50 and marks >=40):
    print("Grade is C")
else:
    print("Grade is D")

#Assignment 2
#Prime Number Nested Loop
for Number in range (1, 1000):
    count = 0
    for i in range(2, Number):
        if(Number % i == 0):
            count = count + 1
    if (count == 0 and Number != 1):
        print(Number)
#Assignment 3
#Table Generation
for it in range(1,11):
    for mul in range(1,11):
        count = mul*it
        print(it," ", "X"," ",mul, " ","="," ",count)
    print("\t")


#Assignment 4
#prime number using while
user_input = int(input("Please enter number till you want to print Prime Number"))
Number =1

while (Number<=user_input):
    count=0
    i=2
    
    while (i<=Number):
        if (Number%2==0):
            count= count+1
            break
        i = i+1
    if count ==0 and Number!=1:
        print(Number)
    Number = Number + 1
