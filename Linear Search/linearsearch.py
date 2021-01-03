def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
    
def main():
    arrayList = [2, 14, 23, 34, 35, 57, 62, 67, 78]
    itemIndex = linear_search(arrayList, 35)
    if itemIndex != -1:
        print("The index of the required item is: {}".format(itemIndex))
    else:
        print("Item not found")
    
if __name__ == "__main__":
    main()