#Regular Expression
import re 

while True:
    string=raw_input("Enter any string\n")
    print "Input ->",string

    if string=='end':
        break

    print "-----------------------------------------------"

    #simple match
    if re.search('python',string,re.I):#re.I/re.IGNORECASE-ignore case
        print "python is present"
    else:
        print "python not found"
    print "-----------------------------------------------"
    #Anchors (^ and $)
    #^-startswith
    if re.search('^python',string):
        print "^python - satisfied"
    else:
        print "^python - not satisfied"
    #$endswith    
    if re.search('python$',string):
        print "python$ - satisfied"
    else:
        print "python$ - not satisfied"
    #empty string
    if re.search('^$',string):
        print "^$ - satisfied"
    else:
        print "^$ - not satisfied"
    #exact match
    if re.search('^python$',string):
        print "^python$ - satisfied"
    else:
        print "^python$ - not satisfied"

    print "-----------------------------------------------"
    #range of char- [0-9],[a-z],[A-Z]
    if re.search('^[0-9][A-Z][a-z]$',string):
        print "^[0-9][A-Z][a-z]$ - satisfied"
    else:
        print "^[0-9][A-Z][a-z]$ - not satisfied"
    print "-----------------------------------------------"

    #metacharacters
    # + => One or More Occurences
    # * => Zero or More occurences
    # ? => Zero or one occurence

    if re.search('^ab+c$',string):
        print "^ab+c$ -satisfied"
    else:
        print "^ab+c$ - not satisfied"
    if re.search('^ab*c$',string):
        print "^ab*c$ -satisfied"
    else:
        print "^ab*c$ - not satisfied"
    if re.search('^ab?c$',string):
        print "^ab?c$ -satisfied"
    else:
        print "^ab?c$ - not satisfied"
    if re.search('^a[a-z]+c$',string):
        print "^a[a-z]+c$ -satisfied"
    else:
        print "^a[a-z]+c$ - not satisfied"    
    print "-----------------------------------------------"        

    #quantifiers
    # {m} => Matches exactly 'm' occurences
    # {m,n} => Minimum 'm' and Max 'n' occurences
    if re.search('^ab{2}c$',string):
        print "^ab{2}c$ -satisfied"
    else:
        print "^ab{2}c$ - not satisfied"
    if re.search('^ab{1,3}c$',string):
        print "^ab(1,3}c$ -satisfied"
    else:
        print "^ab(1,3}c$ - not satisfied"
    print "-----------------------------------------------"

     #Grouping
    if (re.search('^(ab){2}c$',string)):
        print "^(ab){2}c$ is staisfied"
    else:
        print "^(ab){2}c$ is not satisfied"
    print "-----------------------------------------------"        

    #Alternative and choices
    if (re.search('^a[bcd]e$',string)):
        print "^a[bcd]e$ is staisfied"
    else:
        print "^a[bcd]e$ is not satisfied"
    if (re.search('^a[^bcd]e$',string)): #[^bcd]--except bcd
        print "^a[^bcd]e$ is staisfied"
    else:
        print "^a[bcd]e$ is not satisfied"
        
    print "-----------------------------------------------"
    
    #Dot character - matches any single character
    if (re.search('^a.c$',string)):
        print "^a.c$ is staisfied"
    else:
        print "^^a.c$ is not satisfied"    
    if (re.search('^a.*c$',string)):
        print "^a.*c$ is staisfied"
    else:
        print "^^a.*c$ is not satisfied"
    print "-----------------------------------------------"

    #characte class escape sequences
    #\d => [0-9]; \D => [^0-9]
    #\w => [0-9a-zA-Z_]; \W => [^0-9a-zA-Z_]
    #\s => Space/Tab ; \S => Other than space or tab

    if re.search('^(\d{4}\s){2}\d{4}$',string):
        print "Valid Aadhar number"
    else:
        print "Invalid format"
        
