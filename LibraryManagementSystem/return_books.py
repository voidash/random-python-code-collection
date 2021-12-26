import listsplit
import re
import os
from datetime import date, datetime

fine = 0
def has_user_borrowed(fname):
    return os.path.exists(f"Borrower_{fname}.txt")


isbn_kv = listsplit.isbn_kv
def read_borrowed_books(fname):
    # borrowed book list from file
    global bbl_file
    bbl_file = dict() 
    with open(f"Borrower_{fname}.txt") as f:
        line = f.readline()
        while line:
            if re.search(r"^Total.+",line):

            else:
                temp_list = (line.split(","))
                bbl_file[temp_list[1]] = temp_list[2:]

            line = f.readline() 
        

def check_for_fine(isbn):
    global fine 
    current_date = datetime.now()
    previous_date = datetime.strptime(bbl_file[isbn][2][:10],"%Y-%m-%d")
    elapsed_time = current_date - previous_date
    if elapsed_time.days > 30:
        fine+=4
    return elapsed_time.days > 30

def return_books(fname,isbn):
    listsplit.rewrite_library([isbn],True)
    write_to_returned_file(fname,'1')



def write_to_returned_file(fname,isbn):
    # Returned_fname.txt
    with open(f"Returned_{fname}.txt",'a') as f:
        f.write(f"{fname},{isbn},{bbl_file[isbn][1]},{datetime.now()} \n")
        f.write(f"Total Paid Price: {fine+int(bbl_file[isbn][1].strip()[1:])} \n")
        

     


def return_book_for_main():
    fname = input("enter your first  name >>> ")

    if not has_user_borrowed(fname):
        raise Exception("User file not found")
    
    read_borrowed_books(fname)
    print("These are the books you have borrowed")
    print(bbl_file)

    while True:
        isbn = input("enter isbn number >> ")
        if not isbn in bbl_file.keys():
            raise Exception("You haven't borrowed the book of that ISBN number")
        if check_for_fine(isbn):
            print("since you haven't returned book for 30 days , you will be fined")
        return_books(fname,isbn)
        yes_no = input("do you want to return other books >> ")
        if yes_no.lower() == 'n':
            break
    




        

    



