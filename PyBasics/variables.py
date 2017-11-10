print "Hello-Welcome to python"
print "----------------------------"
#Dynamic Type

var=5
print var,'->' ,type(var)
var=1.5
print var,'->' ,type(var)
var='A'
print var,'->' ,type(var)
var='python'
print var,'->' ,type(var)
print "----------------------------"

VAR='Python is so much efficient'
print var
print VAR
VAR="Python is so much efficient"
print VAR
VAR="'Python' is so much efficient"
print VAR
VAR="\"Python\" is so much efficient"
print VAR
VAR='"Python" is so much efficient'
print VAR
print "----------------------------"
#comments
#single line comment
'''multiple
line or block level
comments
'''
multi_line_str="""
line1
line2
line3
"""
print multi_line_str
print "----------------------------"
#Multiple assignment
num1=num2=num3=5
print "Number1->",num1
print "Number2->",num2
print "Number3->",num3

num,float_num,str1=1,1.5,"Python"

print num,float_num,str1
print "----------------------------"

#in 3.6
'''
print (num,float_num,str,sep=',',end='|')

output: 5,5,5(instead 5 5 5)
sep & end are keyword parameter
'''
print "----------------------------"

input=raw_input("Enter the value")
print input,'->',type(input)
#input value always ll be a string type
#if you want to convert we need type cast
input1=int(raw_input("Enter the value"))
print input1,'->',type(input1)

inp=input("Enter a value:")
print inp,'->',type(inp)
inp=input("Enter a str value:")
print inp,'->',type(inp)
print "----------------------------"
