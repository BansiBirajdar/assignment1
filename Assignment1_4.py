'''Write a program which display 5 times Marvellous on screen.
Output : Marvellous
         Marvellous
         Marvellous
         Marvellous
         Marvellous'''
def display(no):
    for i in range(0,no):
        print("\tMarvellous")

def main():
    no=int(input("Enter the number how many time display="))
    display(no)
    
if(__name__=="__main__"):
    main()