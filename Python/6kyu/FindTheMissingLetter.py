'''
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
'''

# Time: 489ms Passed: 33 Failed: 0
def find_missing_letter(chars):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    shrt_alpha = alphabet[:len(chars)]
    missing_letter = ""
    sliced_part = []

    for k, v in enumerate(alphabet):
        if chars[0].lower() == alphabet[k]:
            sliced_part = alphabet[k:k+len(chars)]


    for k, v in enumerate(chars):
        if chars[k].lower() != sliced_part[k]:
            missing_letter = sliced_part[k]
            break

    if chars[0].isupper():
        print(missing_letter.upper())
        return missing_letter.upper()
    else:
        print(missing_letter)
        return missing_letter
