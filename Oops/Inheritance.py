#Inheritance
'''
inherit the properties of base class
4 types:
=>single inheritance - one base -> one derived
=>multi level
    A
    |
    B
    |
    C
=>multiple
    A   B
     \ /
      C
=>hierarchial
     A
    / \
   B   C
'''
print "------------------------------------"
print "Single Inheritance"

class SI1():
    def __init__(self):
        print "In SI1"

class SI2(SI1):
    #pass
    def __init__(self):
        print "In SI2"

objSI2=SI2()

class SI1():
    def __init__(self):
        print "In SI1"

class SI2(SI1):
    pass
    '''def __init__(self):
        print "In SI2"'''

objSI2=SI2()#It will call parent

print "------------------------------------"

print "Hierarchial Inheritance"
class HR1():
    def __init__(self):
        print "In HR1"

class HR2(HR1):
    #pass
    def __init__(self):
        print "In HR2"

class HR3(HR1):
    #pass
    def __init__(self):
        print "In HR3"

objHR2=HR2()
objHR3=HR3()

class HR1():
    def __init__(self):
        print "In HR1"

class HR2(HR1):
    #pass
    '''def __init__(self):
        print "In HR2"'''

class HR3(HR1):
    #pass
    '''def __init__(self):
        print "In HR3"'''

objHR2=HR2()
objHR3=HR3()
print "------------------------------------"

print "Multilevel Inheritance"

class MI1():
    def __init__(self):
        print "In MI1"

class MI2(MI1):
    #pass
    def __init__(self):
        print "In MI2"

class MI3(MI2):
    #pass
    def __init__(self):
        print "In MI3"

objMI2=MI2()
objMI3=MI3()

class MI1():
    def __init__(self):
        print "In MI1"

class MI2(MI1):
    #pass
    def __init__(self):
        print "In MI2"

class MI3(MI2):
    pass
    '''def __init__(self):
        print "In MI3"'''

objMI2=MI2()
objMI3=MI3()

class MI1():
    def __init__(self):
        print "In MI1"

class MI2(MI1):
    pass
    '''def __init__(self):
        print "In MI2"'''

class MI3(MI2):
    pass
    '''def __init__(self):
        print "In MI3"'''

objMI2=MI2()
objMI3=MI3()
print "------------------------------------"

print "Multiple Inheritance"

class MPI1():
    def __init__(self):
        print "In MPI1"

class MPI2():
    #pass
    def __init__(self):
        print "In MPI2"

class MPI3(MPI1,MPI2):
    #pass
    def __init__(self):
        print "In MPI3"

objMP3=MPI3()

class MPI1():
    def __init__(self):
        print "In MPI1"

class MPI2():
    #pass
    def __init__(self):
        print "In MPI2"

class MPI3(MPI1,MPI2): # call MPI1
    pass
    '''def __init__(self):
        print "In MPI3"'''

objMP3=MPI3()

#o/p : In MPI1

class MPI1():
    def __init__(self):
        print "In MPI1"

class MPI2():
    #pass
    def __init__(self):
        print "In MPI2"

class MPI3(MPI2,MPI1): # call MPI2
    '''def __init__(self):
        print "In MPI3"'''
    pass

objMP3=MPI3()

#To know base classes of a particular class
print "Bases->",MPI3.__bases__
print "Bases->",objMP3.__class__
print "Doc->",MPI3.__doc__
print "Doc->",__doc__
print "class name->",MPI3.__name__ #MPI3
print "Module->",__name__ #__main__

#if __name__='__main__':

#o/p : In MPI2
print "------------------------------------"        
