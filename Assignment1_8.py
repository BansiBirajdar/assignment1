''' Write a program which accept number from user and print that number of “*” on screen.
    Input : 5 Output : * * * * *'''

def Display(no):
    print(" output=",end=" ");
    for i in range(0,no):
        print("*\t",end=" ");
        
def main():
    no=int(input("Enter the number how many time print \'*\'= "));
    Display(no);
    
if(__name__=="__main__"):
    main();