"""
Given a string, return the count of the number of times that a substring length 2 appears in the
string AND also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""

def last2(inputString):
    #grab the last two characters
    last2_chars = inputString[-2:]
    count = 0
    test_string = inputString[:-2]
    len_test_string = len(test_string)
    loop_iter = len(inputString) - 2

    #this grabs everything BUT the last two chars
    len_inputString = len(inputString)
    for x in range(loop_iter):
        #check every two chars
        if (inputString[x] + inputString[x+1]) == last2_chars:
            count += 1
    # exclude last occurrence

    return count



x = last2('axxxaaxx')
print(x)

