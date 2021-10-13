'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

'''

def namelist(names):
    # arr is short for array
    arr = []
    arr2 = []
    for each in names:
        for k, v in each.items():
            arr.append(v)

    if len(arr) > 1:
        arr2.append(arr[0:-1])
        arr2.append("&")
        arr2.append(arr[-1])
    
    elif len(arr) == 2:
        arr2.append(arr[0])
        arr2.append("&")
        arr2.append(arr[1])
    
    elif len(arr) == 1:
        for each in names:
            for k, v in each.items():
                print(v)
                return v
    else:
        return ""

    result = []
    result.append(', '.join(arr2[0])) 
    result.append(arr2[-2])
    result.append(arr2[-1])

    return ' '.join(result)
