import pprint as pp
with open ("image.png","rb") as file:

    for i in file.readlines()[2:3]:
        pp.pprint(hex(i))
        

