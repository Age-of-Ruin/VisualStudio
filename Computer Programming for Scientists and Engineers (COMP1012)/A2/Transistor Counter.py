# Transistor Count (Moores Law)

year1 = 1970
count1 = 1000
year2 = 1970
count2 = 1000

AvgNeurons = 86 * (10**9)


while count1 < AvgNeurons  :
    
    year1 = year2 + 1
    count1 =  count2 * 1.5
    
    print "Count: %d  " "%d" % (count1, year1)
    
    year2 += 2
    count2 = 2 * count2
    
    print "Count: %d  " "%d" % (count2, year2)
   