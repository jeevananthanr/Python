#Iterator
#While

count=1
while count<=10:
    print count
    count+=1
print "Iteration Completed"

#while with else
while count<=10:
    print count
    count+=1
else:    
    print "Iteration Completed"

#break
while count<=10:
    if count==6:
        break
    print count
    count+=1
else:    
    print "Iteration Completed"  #else statement ll be skipped

#Else statement will be skipped only if control exit in between the loops    

#continue
while count<=10:
    if count==6:
        continue
    print count
    count+=1
else:    
    print "Iteration Completed"  #else statement ll be work     

print "-----------------------------------------"

#for loop

Str="Python"

for ch in Str:
    print "Char->",ch

for word in "Python is so much powerful".split():
    print "word->",word


#Range()
    n=10
for i in range(n): #stars from 0 to n-1
    print i
print "Iteration Completed"


for i in range(1,n):#start and end range
    print i
print "Iteration Completed"


for i in range(1,n,2):#start and end range and increment
    print i
print "Iteration Completed"

for i in range(n,0,-1):#start and end range and increment
    print i
print "Iteration Completed"

print "-----------------------------------------"
