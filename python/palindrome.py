def revstring(string):
    backwards = ""  # String variable that will hold the reversed string parameter
    strlist = list(string)  # Convert parameter into a list
    for i in range(len(strlist), 0, -1):  # Loop through the new list backwards
        backwards += strlist[i-1]  # Add each letter in the parameter into the reversed string variable
    return backwards


def isitapalindrome(string):
    # If the String parameter is the same forwards and backwards...
    if revstring(string).casefold().replace(" ", "") == string.casefold().replace(" ", ""):
        print("'" + string + "' is a palindrome")  # ...it is a palindrome
    else:
        print("'" + string + "' is NOT a palindrome")


isitapalindrome(input("Enter string: "))
