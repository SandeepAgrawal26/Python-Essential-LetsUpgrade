#Assignment 1
#File Read and Write
test = open("Assignmentday5.txt",'w')
test.write("I Love Let's Upgrade. ")
test.close()

test=open("Assignmentday5.txt",'r')
content=test.read()
print(content)
test.close()

test=open("Assignmentday5.txt",'a')
test.write(" keep up the good work!!!")
test.close()


#Assignment 2
#Print factorial
def fact(Number):
    n=1
    while Number>0:
        n=n*Number
        Number = Number-1
    print(n)