#File handling

#fname="Sample.txt"
#fname="C:\\Users\\A603367\\Desktop\\Py\\File\\Sample.txt"
fname="C:/Users/A603367/Desktop/Py/File/Sample.txt"
#open

fhandle=open(fname,"w") #'''create if its not exist otherwise overwrite'''

#lst=['hello','hai']
#write content
fhandle.write("Welcome to File handling\n")
fhandle.write("________________________\n")
fhandle.write("Hello!\n")
#fhandle.write(lst)

#file append

fhandle1=open(fname,"a")
fhandle1.write("Appended!")

#close
fhandle.close()
fhandle1.close()
print "File Created"

print "_________________________________________________________"

#Read mode

fread=open(fname)

#read, readline and readlines()
print "Using read->",fread.read(25)
print "Using readline->",fread.readline()
print "Using readlines->",fread.readlines()
fread.seek(0)
print "readline slice->",fread.readlines()[2:3]
fread.seek(0)

for rd in fread.readlines():
    print rd

''' other modes
binary mode
read -write r+,w+,a+
'''
