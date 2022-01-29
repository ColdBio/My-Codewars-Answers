'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

'''


# I feel dirty for coming up with this solution, but, ¯\_(ツ)_/¯...
def order(sentence):
    tmp = {}
    num = 0
    result = {}
    count = 0
    final = ""
    for i in sentence.split():
        for j in i:
            if j.isdigit():
                num = j
                tmp[i] = num
                break

    x = sorted(tmp.values())

    for i in x:
        for j in tmp.keys():
            if tmp[j] == i:
                result[j] = tmp[j]


    for k, v in result.items():
        final += k + " "

    return final[:-1]
