'''Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display “Even number” 
otherwise display “Odd number” on console.
    Input : 11   Output : Odd Number
    Input : 8    Output : Even Number'''
    
def ChkNum(no):
    if(no%2==0):
        print(" \nEven number\n ")
    else:
        print(" \nodd number\n ")
def main():
    no=int(input("Enter the number = "))
    ChkNum(no)

if(__name__=="__main__"):
    main()