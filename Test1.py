#print "Beginning Program..."
#print ""

# THIS IS THE BUBBLESORT FUNCTION
def BubbleSort(array):
    for  x1 in range(len(array)):
        Index2 = 1
        Index1 = 0
        for x2 in range(len(array)-1):
            if array[Index1] > array[Index2]:
                temp = array[Index1]
                array[Index1] = array[Index2]
                array[Index2] = temp
            Index2+=1
            Index1+=1
    return array    

print "Original array:"
Array = [62,34,53,54,47,43,43,33]
print(Array)

print "Sorted Array"
Array = BubbleSort(Array)
print(Array)

            
        
    
                
    
