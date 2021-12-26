def elements():
    global isbn
    global bname
    global author
    global stock
    global price
    bname = []
    author = []
    stock = []
    price = []
    isbn= []
    with open("library.txt","r") as l :
        each_line = l.readlines()
        
        for i in each_line:
            i = i.strip("\n")
            
            index = 0
            
            for a in i.split(","):
                if (index==0):
                    isbn.append((a.strip()))
                elif (index==1):
                    bname.append(a.strip())
                elif (index==2):
                    author.append(a.strip())
                elif (index==3):
                    stock.append(int(a.strip()))
                elif(index==4):
                    price.append(int(a[2:]))
                index = index +1

elements()



    


