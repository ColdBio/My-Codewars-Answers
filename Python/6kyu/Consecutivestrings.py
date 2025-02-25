'''
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).

'''


def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""

    words_in_pairs = [];
    left = 0
    right = k
    
    for i in strarr:
        if right > len(strarr):
            break
        else:
            words_in_pairs.append("".join(strarr[left:right]))
            left+=1
            right+=1

    candidates = words_in_pairs[0]

    for i in words_in_pairs:
        if len(i) > len(candidates):
            candidates = i

    if len(candidates[0]) == 0:
        return ""
    else:
        return candidates
