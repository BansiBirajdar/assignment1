''' Write a program which display first 10 even numbers on screen.
    Output : 2 4 6 8 10 12 14 16 18 20'''

def EvenDisplay(no):
    if(no<=0):
        return 0;
    i=2;
    while(no>0):
        if(i%2==0):
            print(i,end=" ")
            no-=1
        i+=1
def main():
    no=int(input("Enter the number = "))
    no=EvenDisplay(no)
    if(no==0):
        print("please enter the positive number")
    
if(__name__=="__main__"):
    main()