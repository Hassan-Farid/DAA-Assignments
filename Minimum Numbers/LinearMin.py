def findLinearMin(arr):
    '''
        Assigns the first value of the array as minimum and then 
        applies comparison with all other elements in the array
    '''
    
    minval = arr[0]
    for i in range(len(arr)):
        if arr[i] < minval:
            minval = arr[i]
    
    return minval
    
if __name__ == "__main__":
    numbers = input('Enter the numbers for the array, seperated by a comma: ')
    numbers = numbers.split(',')
    numArray = list(map(int, numbers))
    print('The minimum value in the provided array is: {}'.format(findLinearMin(numArray)))   
    