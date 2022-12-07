'''
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases (input -> output):

1, 10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

1, 100 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.

90, 100 --> []
Enjoy it!!
'''
def examine_single_number(num):
    count = 1
    sum = 0
    for each in list(str(num)):
        sum += int(each) ** count
        count += 1

    if sum == num:
        return sum
        
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    if a and b < 10:
        return list(range(a, b+1))
    result = []
    for c, v in enumerate(range(a, b+1), start=1):
        if examine_single_number(v) != None:
            result.append(examine_single_number(v))

    return result
