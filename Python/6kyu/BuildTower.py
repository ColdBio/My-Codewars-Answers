'''
Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Lua: returns a Table;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
'''

def tower_builder(n_floors):
    arr = []

    '''
    - I'm sure my solution might be overcomplicated and computationally expensive

    - Calculating all odd numbers up to a given floor size
    - For examlpe, if the floor size is 3, then the first 3 odd numbers in a infinite list of odd whole numbers are determined.
    - create a list such that each element is n-many '*' according to their respective odd number at each indez
    '''
    for each in range(1, n_floors+1):
        arr.append("*" * ((each * 2) - 1))

    # Append whitespaces to the end of each element according to the max length of the last element
    arr2 = []
    for each in arr:
        dif = len(arr[-1]) - len(each)
        arr2.append(each + (" " * dif))
    
    '''
    - Each element will have a set amount of empty spaces according to the different between the last element and each element
    - Take that difference, for example if the difference is 4, divide is by 2 and shift all elements by 2 such that there is 
      an even number of whhitespaces at the start and end
    '''
    arr3 = []
    for i in range(0, len(arr2)):
        dif = len(arr[-1]) - len(arr[i])
        x = list(arr2[i])[-int(dif/2):] + list(arr2[i])[:-int(dif/2)]
        arr3.append(''.join(x))

    return arr3
