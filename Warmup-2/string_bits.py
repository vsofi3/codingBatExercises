"""

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(inputString):
    len_inputString = len(inputString)
    newString = ""
    if len_inputString <= 1:
        return inputString
    else:
        for x in range(0, len_inputString, 2):
            newString += inputString[x]
    return newString

x = string_bits('Hello')
print(x)