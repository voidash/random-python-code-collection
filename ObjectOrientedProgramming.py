
#Blog post URL:https://lerner.co.il/2014/10/14/python-attributes/
#Blog post title :In Python, it’s all about the attributes
#attributes(features)


'''
key takeaway


Everything in python is object. 
Functions,classes,dataType 
Every objects have attributes.

Classes execute instantly it is called but function block is executed only when invoked
'''

'''
Question raised
Some built-in classes don't allow addition of attributes
How to implement such functionality?


'''




'''
terminologies unfamiliar with:
instance attribute ,
class attribute ,

ideas unfamiliar with:
Everything in python is object. 

Every objects are attributes

'''

#class attribute : defined outside __init__ and accessible to all the methods in the class
#variable that belongs to class as a whole rather than a specific instance


#instance attribute: variable specific to that particular instance only


class Foo(object):
  wage_increase = 10  #acts like class attribute

  def __init__(self,x,y):
    self.x=x    #acts like instance attribute
    self.y=y
    
  


#attributes of the object can be accessed by dir()
i=123
len(dir(i))
#64
dir(i)[:5] 
#['__abs__', '__add__', '__and__', '__class__', '__cmp__']


'''
get_attr() : 2 arguments : instanceReference attributeOfthatInstance 
and 
set_attr() : 3 arguments : instanceReference attributeOfThatInstanceToInvoke valueForThatAttribute
'''

'''

.(dot) operator is used instead of get_attr and set_attr

'''


