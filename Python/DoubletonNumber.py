''' 
We will call a natural number a "doubleton number" if it contains exactly two distinct digits. For example, 23, 35, 100, 12121 are doubleton numbers, and 123 and 9980 are not.

For a given natural number n (from 1 to 1 000 000), you need to find the next doubleton number. If n itself is a doubleton, return the next bigger than n.

Examples:
doubleton(120) == 121
doubleton(1234) == 1311
doubleton(10) == 12

This solution is exceedingly complicated. I will try to redo this in future after some more practice.

'''
def doubleton(num):
    x = num
    x = x + 1
    temp = [int(each) for each in str(x)]
    temp2 = set(temp)
    print(len(temp))
    if len(temp2) == 1:
        while x < 10:
            x = x + 1
        temp3 = [int(each) for each in str(x)]
        if temp3[0] != temp3[1]:
            return x
        else:
            print(x + 1)
            return x + 1
    elif len(temp2) == 2:
        print(x)
        return x
    elif len(temp2) > 2:
        for i in range(0, 1000000):
            x = x + 1
            temp = [int(each) for each in str(x)]
            temp2 = set(temp)
            if len(temp2) == 2:
                print(x)
                return x
