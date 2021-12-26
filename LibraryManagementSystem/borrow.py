import dt
import listsplit

def borrowbook():
    book = listsplit.isbn
    borrowedbooklist = []
    instock = listsplit.stock
    found = True
    while(True):
        fname = input("Enter your first name.")
        if(fname.isalpha()):
            break
        else:
            print("Please enter valid first name.")
    while(True):
        lname= input("Enter you last name.")
        if(lname.isalpha()):
            break
        else:
            print("Please enter valid last name.")

    while(True):
        ask = input("Enter the ISBN of the book you want to borrow.")
        
        index = 0 
        for b in book:
            if (b == ask):
                print("Book found sucessfully.")
                borrowedbooklist.append(index)
            index = index + 1
        print(index)

borrowbook()
            



