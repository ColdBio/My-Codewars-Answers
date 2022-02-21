'''
Given a triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]
Note: your code should be optimized to handle big inputs.
'''
def odd_row(n):
    # Formula for determing the first element in the array
    calc = ((n * n) - n) + 1
    result = [calc]
    for each in range(0, n-1):
        calc += 2
        result.append(calc)

    return result
