'''
Title: Enumerable Magic #20 - Cascading Subsets

Create a method each_cons that accepts a list and a number n, and returns cascading subsets of the list of size n, like so:

each_cons([1,2,3,4], 2)
  #=> [[1,2], [2,3], [3,4]]

each_cons([1,2,3,4], 3)
  #=> [[1,2,3],[2,3,4]]
  
'''
# This definitely was should not be an 8kyu problem

def each_cons(lst, n):
    l = 0
    r = n
    tmp = []

    if n == 1:
        for each in lst:
            tmp.append([each])

    for each in range(0, len(lst)):
        if len(tmp) == len(lst):
            break
        if len(lst[l:r]) == n:
            tmp.append(lst[l:r])
        
            l += 1
            r += 1

    return tmp
