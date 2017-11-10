#OOPS

class Account():
    ac_name="jeeva"
    ac_no="123212213"
    ac_branch="Chennai"
    #initialize the obj
    def __init__(self):
        #print "I am in init method"
        self.ac_name="raj"
        self.ac_no="123"
        self.ac_branch="BLR"

#object
print "Creating obj1"        
objAcc1=Account()
print "Creating obj2"
objAcc2=Account()

print "objAcc1->",objAcc1
print "objAcc2->",objAcc2
print "------------------------------"
print "Usig class->",Account.ac_name
print "Using object1->",objAcc1.ac_name
print "Using object1->",objAcc1.ac_no
print "Using obj2->",objAcc2.ac_branch
print "------------------------------"

#passing args and method overloading
class Account1():
    ac_name="jeeva"
    ac_no="123212213"
    ac_branch="Chennai"
    #initialize the obj
    def __init__(self,name='ABC',no='000',branch='Chennai'):
        #print "I am in init method"
        self.ac_name=name
        self.ac_no=no
        self.ac_branch=branch

#object
print "Creating obj1"        
objAcc1=Account1('Katesh')
print "Creating obj2"
objAcc2=Account1('jeeva',12345)
print "Creating obj3"
objAcc3=Account1(branch='CBE')

print "Object1 values:"
print "Using object1->",objAcc1.ac_name
print "Using object1->",objAcc1.ac_no
print "Using obj2->",objAcc1.ac_branch

print "Object2 values:"
print "Using object2->",objAcc2.ac_name
print "Using object2->",objAcc2.ac_no
print "Using obj2->",objAcc2.ac_branch

print "Object3 values:"
print "Using object3->",objAcc3.ac_name
print "Using object3->",objAcc3.ac_no
print "Using obj3->",objAcc3.ac_branch
print "------------------------------"

#__str__(self)
class Account1():
    ac_name="jeeva"
    ac_no="123212213"
    ac_branch="Chennai"
    #initialize the obj
    def __init__(self,name='ABC',no='000',branch='Chennai'):
        #print "I am in init method"
        self.ac_name=name
        self.ac_no=no
        self.ac_branch=branch
    def __str__(self):
        return "{0}-{1}-{2}".format(self.ac_name,self.ac_no,self.ac_branch)

#object
print "Creating obj1"        
objAcc1=Account1('Katesh')
print "ObjAcc1->",objAcc1.ac_name,objAcc1.ac_no,objAcc1.ac_branch
print "Creating obj2"
objAcc2=Account1('jeeva',12345)
print "ObjAcc2->",objAcc2.ac_name,objAcc2.ac_no,objAcc2.ac_branch
print "Creating obj3"
objAcc3=Account1() #uses __Str__() to convert the refernce intp string
print objAcc3

#Private variable
#by default all the variables are public.
#to declare the variale as private prefix with __(double underscore)
class Account1():
    ac_name="jeeva"
    ac_no="123212213"
    ac_branch="Chennai"
    __ac_bal=5000
    #initialize the obj
    def __init__(self,name='ABC',no='000',branch='Chennai',bal=0.0):
        #print "I am in init method"
        self.ac_name=name
        self.ac_no=no
        self.ac_branch=branch
        self.__ac_bal=bal
    def __str__(self):
        return "{0}-{1}-{2}".format(self.ac_name,self.ac_no,self.ac_branch)
    def get_balance(self):
        return self.__ac_bal
    def deposit(self,amt):
        self.__ac_bal+=amt
        return self.__ac_bal
    def withdraw(self,amt):
        self.__ac_bal-=amt
        return self.__ac_bal

#object
#print Account1.__ac_bal --we cant access
obj1=Account1('gva',bal=5000)    
print obj1.get_balance()
print obj1.deposit(1000)
print obj1.withdraw(500)
print obj1.get_balance()
    


