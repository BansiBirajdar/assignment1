''' Write a program which display 10 to 1 on screen.
    Output : 10 9 8 7 6 5 4 3 2 1'''

def Display(no):
    print("output=",end=" ")
    while(no>0):
        print(no,end=" ")
        no-=1

def main():
    no=int(input("Enter the number ="))
    Display(no)


if(__name__=="__main__"):
    main();
    