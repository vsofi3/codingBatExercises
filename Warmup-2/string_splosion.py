"""

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""

"""
this looks like it could be a double for loop?
it iterates the length of the input string 
"""

def string_splosion(inputString):
    new_string = ""
    len_inputString = len(inputString) #len of string will be how many times we iterate
    if len_inputString == 1:
        return inputString
    elif len_inputString == 2:
        new_string = inputString[0] + inputString[0] + inputString[1]
        return new_string
    else:
        start = 1
        for x in range(len_inputString):
            for j in range(start):
                new_string += inputString[j]
            start += 1
    return new_string




x = string_splosion("abc")
print(x)