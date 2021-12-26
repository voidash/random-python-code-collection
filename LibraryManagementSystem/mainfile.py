import borrow
import datetime
def main():
    print("Welcome to the Library Management System.\n")
    condition = True
    while(condition == True):
        print("Enter 1 to display all the books in the library.")
        a = int(input("Enter your choice."))
        print("\n")
        
        if(a == 1):
            print("     Books in this library.\n")
            print(" |ISBN| |Book Name| |Author| |stock||Price|")
            with open("library.txt","r") as o:
                content = o.readlines()
            for line in content:
                print(line)
   
        elif(a > 4):
            raise ValueError("Please enter valid value suggested above.")
try:        
    main()
except ValueError:
    print("That was not a valid number.")
