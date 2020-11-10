def Permute(string):
    '''
        Returns a list of all possible permutations of the provided string parameter
    '''
    
    #Return an empty string list if the provided parameter is of length zero
    if len(string) == 0:
        return ['']
    
    #prevList recursively breaks the string into characters based on their order
    prevList = Permute(string[1:len(string)])
    nextList = []
    
    #Based on the one character left from the previous list, we create the nextList by appending 
    #the previous elements in a loop, so as to create all possible permutations
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j] + string[0] + prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    
    #The final returned result is the list of all possible permutations of the provided string
    return nextList
        

def BruteAnagram(str1, str2):
    '''
        Takes every character in the first string and creates
        different permutations using it. Each permutation is 
        compared with the second string. If any one the permutations
        match the second string, it returns True otherwise False 
    '''
    
    isAnagram = False
    
    #Permutes all possible outcomes from the string
    permList = Permute(str1)

    #Compares every string in the permutation list, if it matches then the value returned is True otherwise False
    for i in permList:
        if i == str2:
            isAnagram = True
        
    return isAnagram 


if __name__ == "__main__":
    str1 = input("Enter the first word: ")
str2 = input("Enter the second word: ")
isAnagram = BruteAnagram(str1, str2)
if isAnagram == True:
    print("Given strings are anagram of each other")
else:
    print("Given strings are not anagram of each other")
