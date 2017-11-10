#Lists
#Collections of elements of diff datatypes
#Mutable

num_lst=list(range(1,6))
print num_lst,'->',type(num_lst)

num_lst=list(range(1,6))+list(range(10,5,-1))
print num_lst,'->',type(num_lst)

#Access of elements of list

print "num_lst[5]->",num_lst[5]
print "num_lst[-5]->",num_lst[-5]

print "num_lst[1:7]->",num_lst[1:7]
print "num_lst[::2]->",num_lst[::2]
print "num_lst[::2]->",num_lst[1::2]
print "num_lst[::2]->",num_lst[::-1]

print "-----------------------------------------------"
#Adding elements to the list
#Append - append the item or list at the end
num_lst.append(3)
print "After appended:->",num_lst

#insert - insert item or list into specific index
num_lst.insert(5,3)
print "After inserted at the index 5:->",num_lst

#extend
num_lst.extend([1,2,3])
print "After extended :->",num_lst

#extend vs append
#if we append a list it ll take a single element
num_lst.append([10,11,12])
print "Append->",num_lst
num_lst.extend([10,11,12])
print "Extend->",num_lst

#Removing elements
#pop()
#Returns the elemtns which is removed

rem_ele=num_lst.pop()
print "element removed->",rem_ele
print "after pop called",num_lst
print "After pop(5)->",num_lst.pop(5)
print "after pop(5) called",num_lst

#count
print "Number of 3 is :->",num_lst.count(3)

#Remove
# it remove specific item we passed
while num_lst.count(3):
    num_lst.remove(3)

print "After remove all 3:->",num_lst
print "No of 3->",num_lst.count(3)

#clear --will work in version 3+
#num_lst.clear

num_lst.reverse()
print num_lst

num_lst.sort()
print num_lst

#reverse sort?
print "-----------------------------------------------------------------"
#Comprehension
#[exp iteration <condition>]
sqr_lst=[num**2 for num in range(1,int(raw_input("enter a value:"))+1) if num%2==0]

print "sqr_lst->",sqr_lst
loc_lst=['Chennai','CBE','BLR','Noida']

len_loc=[len(loc) for loc in loc_lst if(loc.startswith('C'))]
print len_loc

print "-----------------------------------------------------------------"



