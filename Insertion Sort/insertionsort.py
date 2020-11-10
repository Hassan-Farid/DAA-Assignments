def insertionsort(array, order='ascending'):
    
    for j in range(1,len(array)):
        key = array[j]
        i = j-1
        
        if order == 'descending':
            while i >= 0 and array[i] < key:
                array[i+1] = array[i]
                i -= 1
        
        elif order == 'ascending':
            while i >= 0 and array[i] > key:
                array[i+1] = array[i]
                i -= 1
                
        array[i+1] = key
        
    return array
    
array = [3,7,4,9,23,6,43,78,45]
print(insertionsort(array, 'descending'))