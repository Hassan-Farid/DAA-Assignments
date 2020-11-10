def findQuadMin(arr):
    '''
        Sorts the values in the given array in O(n^2) time in ascending order
        and returns the first index value i.e. minimum value
    '''
    
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key 
    
    return arr[0]

if __name__ == "__main__":
    numbers = input('Enter the numbers for the array, seperated by a comma: ')
    numbers = numbers.split(',')
    numArray = list(map(int, numbers))
    print('The minimum value in the provided array is: {}'.format(findQuadMin(numArray)))   
    
    