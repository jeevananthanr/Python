#Dictionary
#key-value pair

emp_dict={}
print emp_dict,"->",type(emp_dict)

dict1={'name':'Ravi',
      'location':'Chennai',
      'salary':'15000'}

print dict

#Name
print "Name ->",dict1['name']
print "-----------------------------------------------------------------"
#key overwritten
dict1={'name':'Ravi',
      'location':'Chennai',
      'salary':'15000',
      'name':'Jeeva'}

print "Name ->",dict1['name']

dict1['name']=['venkat','vasanth','karthi'] #it ll replace the last key if there are dups

print "dict ->",dict1
print "dict['name'] ->",dict1['name']
dict1['name'].append('jeeva')
print "-----------------------------------------------------------------"

dict1['team']='Tech hardening'
print "dict ->",dict1

print "-----------------------------------------------------------------"

del(dict1['name'][0])
del(dict1['team'])
print dict1

print "-----------------------------------------------------------------"
#methods
#keys
print "Keys in dict1->",dict1.keys()

for key in dict1.keys():
    print key,'->',dict1[key]

#Values
print "values in dict1:->",dict1.values()   
for val in dict1.values():
    print val

#items

print "items->",dict1.items()
for item in dict1.items():
    key,value=item
    print key,'->',value
    
print "-----------------------------------------------------------------"

dict2={'company':'Fidelity',
       'project':'TH'}
dict1.update(dict2)
print dict1

print "-----------------------------------------------------------------"

#comprehension
#{key:value iteration <condition>}

loc_lst=['Chennai','CBE','BLR','Noida']

dic_loc={loc:len(loc) for loc in loc_lst if(loc.startswith('C'))}

print dic_loc
