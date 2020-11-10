def CountAnagram(str1, str2):
    '''
        Counts the number of characters in both strings and stores it as a dictionary,
        then compares the values in the dictionary. If values are same, then True is
        returned otherwise False
    '''
    
    isAnagram = False
        
    #We can count the number of every character in the string using the count() method of a string
    #The frequencies for each of the characters can then be stored in a dictionray as indicated
    
    dictStr1 = dict((char, str1.count(char)) for char in set(str1))
    dictStr2 = dict((char, str2.count(char)) for char in set(str2))
    
    if dictStr1 == dictStr2:
        isAnagram = True
    
    return isAnagram 

if __name__ == "__main__":
    str1 = input("Enter the first word: ")
    str2 = input("Enter the second word: ")
    isAnagram = CountAnagram(str1, str2)
    if isAnagram == True:
        print("Given strings are anagram of each other")
    else:
        print("Given strings are not anagram of each other")
    
     