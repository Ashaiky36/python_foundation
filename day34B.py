#leetcode valid anagram problem

#using frequency dictionary mapping and comparing while handling uppercases and whitespaces
def character_count(string):
    lower_case = string.lower()
    no_whitespace = lower_case.replace(" ", "")
    char_freq = {}
    for char in no_whitespace:
        if char in char_freq:
            char_freq[char] += 1

        else:
            char_freq[char] = 1

    return char_freq   


string1 = "Dormitory"
res1 = character_count(string1)
print(res1)

string2 = "Dirty Room"
res2 = character_count(string2)
print(res2)

if res1 == res2:
    print("both strings form a valid anagram")

#using counter
from collections import Counter
S1 = "silent"
S2 = "listen"
if Counter(S1) == Counter(S2):
    print("S1 and S2 are valid anagrams")


