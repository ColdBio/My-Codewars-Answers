'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

'''
def solution(s):
    final = []

    for each in s:
        if each.isupper():
            final.append(" ")
            final.append(each)
        else:
            final.append(each)

    return ''.join(final)

