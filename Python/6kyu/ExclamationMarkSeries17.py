"""
Description:

Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".

Examples

balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"

"""
def balance(left, right):
    r = 0
    l = 0
    
    for each in left:
        print(each)
        if each == "!":
            l += 2
        elif each  == "?":
            l += 3

    for each in right:
        if each == "!":
            r += 2
        elif each  == "?":
            r += 3
    
    if r == l:
        return "Balance"
    elif r > l:
        return  "Right"
    else:
        return "Left"
