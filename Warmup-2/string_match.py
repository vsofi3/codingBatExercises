"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""

def string_match(a,b):
    # we will need a double for loop
    count = 0
    len_stringB = len(b)
    len_stringA = len(a)
    if len_stringB > len_stringA:
        #go with smaller string
        go_len = len_stringA
    else:
        go_len = len_stringB
    for x in range(go_len-1):
        if a[x] == b[x] and a[x+1] == b[x+1]:
            count += 1
    return count

x = string_match('xxcaazz', 'xxbaaz')
print(x)