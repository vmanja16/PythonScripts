import sys, re, os



def getAgeFromFunction(Name):

    pattern = re.compile('(\w+)\s*=\s*(\d+)')

    try:
        file = open(os.path.join('C:\Users\Vikram\Desktop\Ages.txt.txt'), 'r')
    except IOError as details: 
        print details
    List = re.findall(pattern, file.read())

    Dictionary = dict(List)

    print "%s's age is %s." % (Name, Dictionary[Name])
    return

#Main body
while True:
    Name = str(raw_input('Who\'s age would you like to know? Type \'exit\' to quit.\n>'))
    if Name.lower() in ['exit','quit']:
        print "Exiting Program"
        break
    try:
        getAgeFromFunction(Name)
    except:
        print "Could not find the age of %s!" %Name
        



    
    
