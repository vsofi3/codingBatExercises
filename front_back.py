"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


def front_back(inputString):
    len_string = len(inputString)

    answer = []
    if len_string == 1:
        return inputString
    elif len_string == 2:
        return inputString[1] + inputString[0]
    else:
        for x in range(len_string):
            answer.append(inputString[x])
            "print(answer[x])"
        first_letter = inputString[0]
        "print(first_letter)"
        answer[0] = inputString[len_string-1]
        answer[len_string-1] = first_letter
        "print(answer[len_string-1])"
        new_print = ""
        for j in range(len_string):
            "add array elements to a string"
            new_print += answer[j]
        return new_print


toot = front_back("keep")
print(toot)