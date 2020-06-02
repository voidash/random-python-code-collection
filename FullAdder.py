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
    dataFeed=zip(a[::-1],b[::-1])
    return output(dataFeed)

def output(dataFeed):
    carry = 0
    sum=0
    d=[]
    #print(dataFeed)
    for data in dataFeed:
        sum,carry = FullAdder(*data,carry).eval()
        d.append(sum)
    d.append(carry)
    return d[::-1]


#main loop
flag = True
while flag:
    num1 = int(input())
    num2 = int(input())
    print(inpOutLoop(num1,num2))
    flagCheck=input("Another one(y/n)")
    if flagCheck == 'n': 
        flag = False
