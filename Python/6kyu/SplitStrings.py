'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
'''
def solution(s):
    final = []
    l=0
    r=2
    if len(s) % 2 == 0:
        for each in s:
            final.append(s[l:r])
            l = r
            r += 2
            final = final[0:int(len(s)/2)]
        return final
    else:
        for each in s:
            print(s[l:r])
            final.append(s[l:r])
            l = r
            r += 2
            final = final[0:int(len(s)/2)+1]
        final[-1]+= "_"
        return final
