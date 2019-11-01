''' Write a program which contains one function named as Add() which accepts two numbers
    from user and return addition of that two numbers.
    Input : 11 5    Output : 16'''
def Add(no1,no2):
    ans=no1+no2
    return ans

def main():
    no1=int(input("enter the first number="))
    no2=int(input("enter the second number="))
    ans=Add(no1,no2)
    print("Addition is =",ans)
if(__name__=="__main__"):
    main()