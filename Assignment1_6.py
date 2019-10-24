''' Write a program which accept number from user and check whether that number is positive or
    negative or zero.
    Input : 11 Output : Positive Number
    Input : -8 Output : Negative Number
    Input : 0 Output : Zero'''
    
    
    
def CheckNum(no):
    if(no==0):
        print("Number is Zero.");
    elif(no>0):
        print("positive Number");
    else:
        print("Negative Number");
        Assignment1_6.py
        
def main():
    no=int(input("Enter the number="));
    CheckNum(no);
    
if(__name__=="__main__"):
    main();