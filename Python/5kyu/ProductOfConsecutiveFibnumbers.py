'''
  The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.

Some Examples of Return:

(depend on the language)

productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false), 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true], 
productFib(800) # should return [34, 55, false], 
-----
productFib(714) # should return {21, 34, 1}, 
productFib(800) # should return {34, 55, 0},        
-----
productFib(714) # should return {21, 34, true}, 
productFib(800) # should return {34, 55, false}, 
Note:

You can see examples for your language in "Sample Tests".
'''

def productFib(prod):
    starting_arr = [0, 1]
    l = 0
    r = 1    
    sum = 0
    result = []

    for each in range(0, prod):
        starting_arr.append(starting_arr[l] + starting_arr[r])
        l += 1
        r += 1

        if starting_arr[-1] > prod:
            l = 0
            r = 1
            break

    for each in range(0, len(starting_arr) - 1):
        sum = starting_arr[l] * starting_arr[r]

        if sum == prod:
            result.append(starting_arr[l])
            result.append(starting_arr[r])
            result.append(True)
            break

        elif sum > prod:
            result.append(starting_arr[l])
            result.append(starting_arr[r])
            result.append(False)
            break

        l += 1
        r += 1

    return result
