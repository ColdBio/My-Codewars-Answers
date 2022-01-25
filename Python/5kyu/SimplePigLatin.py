
'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

'''


def pig_it(text):
    text_array = text.split()
    tmp = 0
    result = ""
    for k, v in enumerate(text_array):
        if len(text_array[k]) > 1:
            x = text_array[k][1:] + text_array[k][0] + 'ay' + " "
            result += x

        if len(text_array[k]) == 1 and text_array[k].isalpha():
            x = text_array[k] + 'ay' + " "
            result += x

        if text_array[k].isalpha() == False:
            result += text_array[k]

    return result.strip()
