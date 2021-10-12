'''
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
'''

# The code below looks like utter mess, will clean this up later, hopefully.

import re
def decipher_this(string):

    arr = []
    for each in re.findall(r'[A-Za-z]+|\d+| ', string):
        try:
            x = chr(int(each))
            arr.append(x)
        except ValueError:
            arr.append(each)
    
    new_string = ''.join(arr)
    arr2 = []
    for each in new_string.split():
        arr2.append(list(each))
        arr2.append(' ')

    final = []
    for each in arr2:
        if len(each) > 2:
            each[1], each[-1] = each[-1], each[1]
            final.append(each)        
        else:
            final.append(each)

    flat_list = [num for sublist in final for num in sublist]
    return ''.join(flat_list).strip()
