#Author : ashish Thapa

#Create your own datatype
class Bin(object):

    def __init__(self,data):
        #check the types first 
        if isinstance(data,int):
            #converts integer into binary
            
            if data >= 2:
                self.bundle =[]
                binary = bin(data)[2:]
                for b in binary:
                   self.bundle.append(Bin(int(b)))
            else:
                self.data = data
        else:
            print("Not a valid data type")
    def __add__(self,other):
        return self.data+other.data
    def __or__(self,other):
        return self.data | other.data
    def __xor__(self,other):
        return self.data ^ other.data
    def __repr__(self):
        return str(self.data)
    
    #add and subtract dunders


class BaseGate:
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def eval(self):
        pass

class AndGate(BaseGate):
    def __init__(self,left,right):
        super().__init__(left,right)

    def eval(self):
        return self.left and self.right



class OrGate(BaseGate):
    def __init__(self,left,right):
        super().__init__(left,right)

    def eval(self):
        return self.left | self.right

class XorGate(BaseGate):
    def __init__(self,left,right):
        super().__init__(left,right)

    def eval(self):
        return self.left ^ self.right


class derivedGates:
    def __init__(self,inputVal):
        self.inputVal = inputVal
    def eval(self):
        pass

class FullAdder(derivedGates):
    def __init__(self,*inputVal):
        super().__init__(inputVal)

    def eval(self):
      A = self.inputVal[0].data
      B = self.inputVal[1].data
      Carry = self.inputVal[2]

      #full adder logic
      x1 = XorGate(A,B)
      x2 = XorGate(x1.eval(),Carry)
      a1 = AndGate(A,B)
      a2 = AndGate(x1.eval(),Carry)
      o1 = OrGate(a1.eval(),a2.eval())
      CarryOut = o1.eval()
      Sum = x2.eval()

      return (Sum,CarryOut)

def inpOutLoop(num1,num2):

    a = Bin(num1)
    b = Bin(num2)
    # this handles the error 
    if hasattr(a,'bundle'):
        a = a.bundle
        
    else:
        a = [a]
    if hasattr(b,'bundle'):
        b = b.bundle
    else:
        b = [b]
      

    lenA = len(a)
    lenB = len(b)
    dataFeed = []
    
    while(len(a) != len(b)):
        a.insert(0,Bin(0)) if lenA<lenB else b.insert(0,Bin(0))
    
    print(" ",strOut(a),"  ",num1)
    print("+",strOut(b),"  ",num2)
    print("_________________")
    dataFeed=zip(a[::-1],b[::-1])
    return output(dataFeed)
def strOut(data):
    
    data = data[:]  #because list is pass by reference we have to make a copy first so that it won't hamper our original array
    flag = False
    while(len(data) != 9):
        data.insert(0,0)
        
        flag = True      
    if flag == True:
        data = data[::-1]
    data = list(map(str,data))[::-1]
    return f'{data[0]}  {"".join(data[1:])}' #data[0] is the one Most significant bit that our 8 bit can't accumulate.
    # if output is greater than 255 then data[0] will act as carry part


def output(dataFeed):
    carry = 0
    sum=0
    d=[]
    #print(dataFeed)
    for data in dataFeed:
        sum,carry = FullAdder(*data,carry).eval()
        d.append(sum)
    d.append(carry)
    while len(d) != 9:
        d.append(0)
    #converting into string for join function to work
    
    decimalEquivalent=0
    for index,singleDigit in enumerate(d):
        decimalEquivalent += singleDigit * (2 ** (index))
    print(f'  {strOut(d)}    {decimalEquivalent}')


#main loop
flag = True
while flag:
    try:
        num1 = int(input("enter 1st Number > ")) 
        num2 = int(input("enter 2nd Number > "))
        if num1 >= 0 and num1 <=255 and num2 >=0 and num2 <=255:
            inpOutLoop(num1,num2)
            flagCheck=input("Another one(y/n)")
            if flagCheck == 'n': 
                flag = False
        else:
            print("enter the value within the constraints")
    except ValueError:
        print("not a valid Number. Try it again")
