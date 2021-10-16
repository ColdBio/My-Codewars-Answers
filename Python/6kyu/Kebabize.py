'''
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters
'''

def kebabize(string):
    tmp = []

    try:
        for each in list(string):
            try:
                if isinstance(int(each), int):
                    pass
            except ValueError:
                if str(each).isupper():
                    tmp.append("-")
                    tmp.append(each)

                else:
                    tmp += each
                
                if tmp[0] == "-":
                    tmp.pop(0)

    except SyntaxError:
        return ''
    
    return ''.join(tmp[0:len(tmp)]).lower()

