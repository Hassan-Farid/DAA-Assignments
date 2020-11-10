def SortAnagram(str1, str2):
    '''
        Sorts both of the strings one at a time and then compares the
        sorted strings. If the strings match then it gives True
        otherwise False
    '''
    
    isAnagram = False
    
    #We can sort the values in the string using the python sorted() method which takes O(n) time
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    if str1 == str2:
        isAnagram = True
    
    return isAnagram

if __name__ == "__main__":
    str1 = input("Enter the first word: ")
    str2 = input("Enter the second word: ")
    isAnagram = SortAnagram(str1, str2)
    if isAnagram == True:
        print("Given strings are anagram of each other")
    else:
        print("Given strings are not anagram of each other")