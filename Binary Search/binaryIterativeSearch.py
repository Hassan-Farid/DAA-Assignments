def binary_search(a, x):
    left, right = 0, (len(a) - 1)
    
    while left <= right:
        middle = (left + right) // 2
        if x > a[middle]:
            left = middle + 1
        elif x < a[middle]:
            right = middle - 1
        else:
            return middle
    return -1
	
def main():
    arrayList = [2, 14, 23, 34, 35, 57, 62, 67, 78]
    itemIndex = binary_search(arrayList, 35)
    if itemIndex != -1:
        print("The index of the required item is: {}".format(itemIndex))
    else:
        print("Item not found")
 
if __name__ == "__main__":
    main()