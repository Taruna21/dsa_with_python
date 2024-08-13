''' Abhay Kanwasi
12:37 AM
Write a Python program to calculate the length of a string.
Click me to see the sample solution

2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
Click me to see the sample solution

3. Write a Python program to get a string made of
 the first 2 and last 2 characters of a given string. 
If the string 
length is less than 2, return the empty string instrsk-aoab-bzn
'''

#Ans1:

#approach_1
def len_of_str(name):
    return len(name)

#approach_2
def length_of_str(string):
    length_of_string = 0
    for char in string:
        length_of_string += 1
    return length_of_string


#Ans2:
def frequency_of_character_in_string(string):
    #google
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char] = 1
    return frequency
        
        
#Ans3
def first_and_last_two_character(string):
    if len(string) < 2:
        return ""
    start = 0
    end = len(string)

    first_two_character = string[start:start+2]
    last_two_character = string[end-2:end]

    return first_two_character + last_two_character




