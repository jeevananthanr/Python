#Map filter and reduce
#Lambda
'''
Ananymous function
one lner fn
can take any number of parametre
eval only one ex
'''

sqr=lambda num:num**2

print "Square -> ",sqr(25)

#map
sqr_lst = map(sqr,range(1,11))

print sqr_lst

print "----------------------------------"
#filter

chk_loc=lambda loc:loc.lower().startswith('c')

all_loc=['chennai','covai','bangalore','pune','cochin']
loc_lst=list(filter(chk_loc,all_loc))
print loc_lst
loc_lst1=list(map(chk_loc,all_loc))
print loc_lst1

print "----------------------------------"
#reduce

#need to import
from functools import reduce

factorial=lambda num1,num2: num1*num2
fact=reduce(factorial,range(1,6))#[1,2,3,4,5]
'''
1*2 =>2
2*3 =>6
6*4 =>24
24*5=>120
'''

print "Factorial->",fact
