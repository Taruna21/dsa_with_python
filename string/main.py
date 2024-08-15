'''
1. Write a Python program to calculate the length of a string.
Click me to see the sample solution

2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
Click me to see the sample solution

3. Write a Python program to get a string made of
 the first 2 and last 2 characters of a given string. 
If the string 
length is less than 2, return the empty string instrsk-aoab-bzn

4. Write a Python program to get a string from a given string where 
all occurrences of its first char have been changed to '$', 
except the first char itself.

5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'

7. Write a Python program to find the first appearance of the
 substrings 'not' and 'poor'
 in a given string. 
If 'not' follows 'poor', replace the whole 'not'...'poor' 
substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'

8. Write a Python function that takes a list of words 
and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9

9. Write a Python program to remove the nth index character from a nonempty string.
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




#Ans5

def get_a_single_string_from_two_given_strings(string1, string2):
    #'abc', 'xyz'
    return string1 + " " + string2

# exa1 = 'abc'
# exa2 = 'xyz'

# result = get_a_single_string_from_two_given_strings(exa1, exa2)
# print(result)


#Ans6

def add_ing_or_ly_in_string(string):
    if string[-1] == "g" and string[-2] == "n" and string[-3] == "i":
        return string + "ly"
    else:
        return string + "ing"

# exa = "abc"
# result = add_ing_or_ly_in_string(exa)
# print(result) 

# exa = "string"
# result = add_ing_or_ly_in_string(exa)
# print(result) 

#Ans7
def find_the_first_appearance_of_the_substrings_not_and_poor(string):
    indices_of_poor = string.find('poor')
    indices_of_not = string.find('not')

    if indices_of_poor > indices_of_not and indices_of_poor>0 and indices_of_not>0:
        return string[:indices_of_not] + 'good'
    else:
        return string

#Ans8
def logest_length_of_words(words):
    #["Taruna", "Damini", "Vishakha"]
    list = []
    for word in words:
        len_of_word = len(word)
        list.append(len_of_word)
    return max(list)

# print(logest_length_of_words(["Taruna", "Damini", "Vishakha"]))


#Ans9
def nth_index_char(string, n):
    #Taruna -> remove r
    return string[:n] + string[n+1:]

# print(nth_index_char(string="Taruna", n=3))
    
#Ans10
def exchange_first_and_last(string):
    before_end = len(string)-1
    return string[-1] + string[1:before_end] + string[0]

print(exchange_first_and_last("Taruna"))

#Ans11