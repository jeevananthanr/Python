#Exception Handling

try:
    num=1/0
except:
    print "Error occured"
print ("After Division")
print "----------------------------"

try:
    num=1/0
except Exception as e:
    print "Error occured ->",str(e)
print ("After Division")
print "----------------------------"

try:
    num=1/0
except Exception as e:
    print "Error occured ->",str(e)
    print "Exception Name ->",e.__class__.__name__
print ("After Division")
print "--------------------------------------------"
try:
    num=1/1
    print string
except ZeroDivisionError as  ze:
    print "Zero deviosion error->",ze
except NameError as ne:
    print "Name error->",ne
except Exception as e:
    print "Error occured ->",str(e)
    print "Exception Name ->",e.__class__.__name__
print ("After Division")
print "--------------------------------------------"

#finally
try:
    num=1/1
    #print string
except ZeroDivisionError as  ze:
    print "Zero deviosion error->",ze
except NameError as ne:
    print "Name error->",ne
except Exception as e:
    print "Error occured ->",str(e)
    print "Exception Name ->",e.__class__.__name__
else:
    print "Else Block Completed Successfully!!"
finally:
    print "this will always be exceuted"
print ("After Division")
print "--------------------------------------------"
#User defined Exceptions

class InvalidNumber(Exception):
    error_msg = "You entered invalid number "
try:
    num=int(raw_input("Enter the number between 50 and 100"))
    if (num>50 and num<100):
        print "Valid Number --> "
    else:
        raise InvalidNumber
except InvalidNumber as e:
    print (e.error_msg, num)

print ("===========Program Completed==============")

'''

