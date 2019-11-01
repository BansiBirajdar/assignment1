'''Write a program which accept name from user and display length of its name.
Input : Marvellous Output :10'''

def Length(name):
    #using len() method
    #print("Given string length is =",len(name))
    #without len() method
    ict=0
    for i in name:
        ict+=1
    return ict


def main():
    name=input("enter the string==")
    L=Length(name)
    if(L==0):
        print("Please enter the string ")
    else:
        print("Given string length is =",L)
    
if(__name__=="__main__"):
    main()