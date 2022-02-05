'''
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
'''


# Time: 502msPassed: 110 Failed: 0
def expanded_form(num):
    result = []
    count = 0

    for each in enumerate(str(num)[::-1]):
        if int(each[1]) * (10 ** count) == 0:
            pass
        else:
            result.append(str(int(each[1]) * (10 ** count)))
        count += 1

    return " + ".join(result[::-1])
