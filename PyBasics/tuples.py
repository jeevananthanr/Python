#Tuples
#constant/immutable list
num_tup=(1,5,'hello','Python',1.5)
print num_tup,"->",type(num_tup)

num_tup=tuple(range(5,11))
#reassign
num_tup=tuple(range(1,11))
print num_tup

#num_tup[5]=10 --will throw an error

#count
print num_tup.count(5)

#index
print num_tup.index(7)
print num_tup.index(7,3)
print num_tup.index(7,3,7)

#len
print len(num_tup)

print min(num_tup)
print max(num_tup)
print sum(num_tup)

#slicing
print num_tup[1:5]
print num_tup[:]
print num_tup[4:]
print num_tup[:6]
print num_tup[::-1]
print "------------------------------"
