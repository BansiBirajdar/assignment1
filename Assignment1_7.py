'''Write a program which contains one function that accept one number from user and returns
    true if number is divisible by 5 otherwise return false.
        Input : 8 Output : False
        Input : 25 Output : True'''

def Div(no):
    if(no%5==0):
        return True
    else:
        return False
def main():
    no=int(input("Enter the number="))
    print("output is {} ".format(Div(no)))
    
if(__name__=="__main__"):
    main()
        
