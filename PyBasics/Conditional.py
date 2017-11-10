#Conditional
#Simple if

if True:
    print "Test IF"
print "After IF"

#If -Else
if 1!=1:
    print "Test IF"
else:
    print "In Else"
print "After IF"

#IF else ladder
num=4
if num==1:
    print "Number is: 1"
elif num==2:
    print "Number is: 2"
elif num==3:
    print "Number is: 3"
else:
    print "Others"
print "After if else ladder"

#pass
if num==1:
    pass
elif num==2:
    print "Number is: 2"
elif num==3:
    print "Number is: 3"
else:
    print "Others"
print "After if else ladder"

#nested
number=125
if number>100:
    if number <150:
        print "number is less than 150"
    else:
        print "number is greater than 150"
else:
    print "number is less than 100"
