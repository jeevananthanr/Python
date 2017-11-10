#operations

#len()
string="I am writing python script"
name_lst=['justin','davies','clark','tries','manual']
num_lst=[10,3,4,6,7,8]
print "-------------------------------------------"
print string
print name_lst
print num_lst

print "Length of the string is ->",len(string)
print "Length id the List->",len(name_lst)

print "-------------------------------------------"
#max() min()
print "Max->",max(name_lst)
print "Min->",min(num_lst)
print "Min->",min(name_lst)
print "Max->",max(num_lst)

print "Sum->",sum(num_lst)
#print "Sum->",sum(name_lst)

print "-------------------------------------------"
#concatenation

print 2+3
print "2"+"3"
print "2+str(3)" #"2"+3 -> error

print "-------------------------------------------"
#repetition op

print 2*3
print "2" *3
print name_lst[1:4] *2

print "-------------------------------------------"
#Membership operator
#in / not in

if "python" in string:  #thon in string also ll work here
    print "Python is present"
else:
    print "Python is not present "

if "davies" not in name_lst:  # dav in name_lst will not work in list
    print "davies is present"
else:
    print "davies not present"
