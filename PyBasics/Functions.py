#Functions

#def function_name(arg_list)

def chk_mail_id(mail_id):
    if len(mail_id)>0:
        if mail_id.endswith('@fmr.com',2):
            print "Valid Mail id"
        else:
            print "Invalid Email id"
    else:
        print "insufficient argument"

#Invoke
chk_mail_id('')
chk_mail_id('jeevar@gmail.com')
chk_mail_id('jeevananthan@fmr.com')
##chk_mail_id()#Error --chk_mail_id() takes exactly 1 argument (0 given)
print "--------------------------------------------------------------"
#return

def chk_mail_id(mail_id):
    if len(mail_id)>0:
        if mail_id.endswith('@fmr.com',2):
            return "Valid Mail id"
        else:
            return "Invalid Email id"
    else:
        return "insufficient argument"

#Invoke
result=chk_mail_id('')
print result
result=chk_mail_id('jeevar@gmail.com')
print result
result=chk_mail_id('jeevananthan@fmr.com')
print result
print "--------------------------------------------------------------"

def chk_mail_id(mail_id):
    status=''
    if len(mail_id)>0:
        if mail_id.endswith('@fmr.com',2):
            status= "Valid Mail id"
        else:
            status= "Invalid Email id"
    else:
        status= "insufficient argument"

    return status        

#Invoke
result=chk_mail_id('')
print result
result=chk_mail_id('jeevar@gmail.com')
print result
result=chk_mail_id('jeevananthan@fmr.com')
print result
print "--------------------------------------------------------------"

#Identity operators -is/is not

# return ll return the value None.
#Invoke
result=chk_mail_id('')
if result is not None:
    print result
result=chk_mail_id('jeevar@gmail.com')
if result is not None:
    print result
result=chk_mail_id('jeevananthan@fmr.com')
if result is not None:
    print result

print "--------------------------------------------------------------"

def chk_mail_id(mail_id):
    status=''
    if len(mail_id)>0:
        if mail_id.endswith('@fmr.com',2):
            status= "Valid Mail id"
        else:
            status= "Invalid Email id"
    else:
        status= "insufficient argument"

    return (status,mail_id)

result,mailid=chk_mail_id('jeevananthanr@fmr.com')
if result is not None:
    print result,mailid

#output:
#Valid Mail id jeevananthanr@fmr.com
print "--------------------------------------------------------------"
#parameters types
#positional parameter
    #-Number of parameters are mandate
    #-Order of parameters are mandate
def display1(name,loc,salary):
    print "Name:->",name
    print "Location:->",loc
    print "Salary:->",salary

display1('jeeva','Chennai',50000)
#display1('chennai',15000)  --TypeError: display1() takes exactly 3 arguments (2 given)

#keyword parameters
#Number of parameters are mandatory
#order of parameters are optional
def display1(name,loc,salary):
    print "Name:->",name
    print "Location:->",loc
    print "Salary:->",salary

display1(name='jeeva',loc='Chennai',salary=50000)
display1(name='jeeva',salary=50000,loc='Chennai')
#display1(name1='jeeva',salary=50000,loc='Chennai')--TypeError: display1() got an unexpected keyword argument 'name1'
#Note the keyword in calling fn should be same as the names used in the arguments list

#Default arguments
#parameters which has default value
#default value should be given in the last

def display3(name,loc='Chennai',salary='10000'):
    print "Name:->",name
    print "Location:->",loc
    print "Salary:->",salary

display3('Mani')
display3('Mani','kochin')
display3('Mani',loc='Hyd',salary='123213')

#def display3(name='ABC',loc,salary='10000'): default value should follow non default
#means default argumets should comes last

#Variable length parameters
# any number of param

#n no. of positional args
def disp_loc(*locations):
    print locations,'->',type(locations)

disp_loc('a','b','c')

#n no. of keyword args
def disp_loc(**details):
    print details,'->',type(details)

disp_loc(name='a',loc='b',sal=5000)

#both

def disp_loc(*locations,**details):
    print locations,'->',type(locations)
    print details,'->',type(details)

disp_loc('x','y','z',
         name='a',
         loc='b',
         sal=5000)

print "--------------------------------------------------------------"
