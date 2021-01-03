def binary_search(array, val):
    if len(array) == 0:
        return -1
    else:
        mid = (len(array)//2)
        if array[mid] == val:
            return mid
        else:
            if val < array[mid]:
                return binary_search(array[:mid], val)
            else:
                return binary_search(array[mid+1:], val)

def main():
    arrayList = [2, 14, 23, 34, 35, 57, 62, 67, 78]
    itemIndex = binary_search(arrayList, 35)
    if itemIndex != -1:
        print("The index of the required item is: {}".format(itemIndex))
    else:
        print("Item not found")

if __name__ == "__main__":
    main()
