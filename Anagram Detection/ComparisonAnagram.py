def CompAnagram(str1, str2):
    '''
        Selects and compares every character in the first string 
        with every other character in the second string. If all
        characters match, it gives True as result otherwise False.
    '''   
    
    isAnagram = False
    matchCount = 0 #Counter variable to count how many total matches have been made per nested loop

    for i in str1:
        for j in str2:
            if i == j:
                matchCount += 1
                break 
    if matchCount == len(str1):
        isAnagram = True
        
    return isAnagram

if __name__ == "__main__":
    str1 = input("Enter the first word: ")
    str2 = input("Enter the second word: ")
    isAnagram = CompAnagram(str1, str2)
    if isAnagram == True:
        print("Given strings are anagram of each other")
    else:
        print("Given strings are not anagram of each other")