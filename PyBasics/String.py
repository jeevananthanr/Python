#String
#String is an immutable obj means we cant add/remove the elements

slogan="python is so much efficient"
print slogan
#indexing
print "slogan[0]->",slogan[0]
print "slogan[-1]->",slogan[-1]
print "slogan[-5]->",slogan[-5]
#slicing
print "slogan[:]->",slogan[:]
print "slogan[1:5]->",slogan[1:5]
print "slogan[:7]->",slogan[:7]
print "slogan[6:]->",slogan[6:]
print "slogan[6:45]->",slogan[6:45]
print "slogan[len(slogan)-2:45]->",slogan[len(slogan)-2:45]
print "slogan[::]->",slogan[::]
print "slogan[1:20:2]->",slogan[1:20:2]
print "slogan[1:20:12]->",slogan[1:20:12]
print "slogan[7::3]->",slogan[7::3]
print "slogan[7::3]->",slogan[::-1]

#palindrome
pal='MadaM'
print "Palindrom?:",pal==pal[::-1]
print "--------------------------------"

#String Methods
print "Capitalize->",slogan.capitalize()
print "Upper->",slogan.upper()
print "Lower->",slogan.lower()
print "Length->",len(slogan)
#check whether string is start with particular word\
#returns boolean
print "Startswith->",slogan.startswith('python')
print "Startswith->",slogan.startswith('thon',2)
print "Endswith->",slogan.endswith('efficient')
print "Endswith->",slogan.endswith('thon',2,6)

print "count(i)->",slogan.count('i')
print "count(i)->",slogan.count('i',-10)

print "Replace->",slogan.replace('much','very')
print "Replace no->","so so so so so so".replace('so','very',3)#1st 3 occurences

#split
#str->list
splt_str=slogan.split(' ')
print splt_str,'->',type(splt_str)
splt_str=slogan.split(' so ')
print splt_str

#strip?

#join
#list->str

jn_str=','.join(splt_str)
print jn_str,'->',type(jn_str)


print "--------------------------------"

