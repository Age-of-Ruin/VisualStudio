# -*- coding: utf-8 -*-
#COMP 1012 A02 Fall 2013
#University of Manitoba Department of Computer Science
#Author:  Robbie Melvin
#Topics:  



#write code that draws a picture... and code that keeps track of that.
#can write a script to create your initial and end list of characters
def createPicture():
    '''creates a string showing a picture of a star using  | / \\ - < >  characters'''
    result = "-----\n"
    for i in range(0,5):
        result += "  ||\n"
    result += "  /\\"    #comment out the lines that draw the actual pictures
    result += "    " 
    result += "\n"       #replace with spaces
    
    result += " <  >"    #that gives you the start up picture
    result += "     "
    result += "\n"  
    
    result += "  \\/"
    result += "     "
    result +="\n"
    #then turn the string into a list.  
    #edit something like this to create the drawing that you want... 
    #then take the resulting list and copy it into your assignment code as contstants
    return list(result)

picture = createPicture()
print picture

print "".join(picture)

#*****************************************
# use the results
#*****************************************

EndPic =   ['-', '-', '-', '-', '-', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '/', '\\', '\n', ' ', '<', ' ', ' ', '>', '\n', ' ', ' ', '\\', '/', '\n']
StartPic = ['-', '-', '-', '-', '-', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', '|', '|', '\n', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '\n']

compare = ""
for i  in range(0, len(EndPic)):
    output =  " %d"% i
    compare +=  (EndPic[i] != StartPic[i]) * output
    
print compare

#*****************************************
# the indicies where the two lists differ... 
# in the assignment you need to carefully set the order
#*****************************************

picIndicies = (33,34,37,40,44,45,46)  

pic = StartPic
print "".join(pic)
for i in picIndicies:
    pic[i] = EndPic[i]
    print "".join(pic)

       