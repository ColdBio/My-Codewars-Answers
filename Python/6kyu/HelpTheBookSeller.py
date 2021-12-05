"""
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which indicates the quantity of books of this code in stock.

For example an extract of a stocklist could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :

M = {"A", "B", "C", "W"} 
or
M = ["A", "B", "C", "W"] or ...
and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.

For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket a list of pairs):

(A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.

If L or M are empty return string is "" (Clojure and Racket should return an empty array/list instead).

Note:

In the result codes and their values are in the same order as in M.

"""


# This code is ugly to look at, but it works \_(•_•)_/
def stock_list(listOfArt, listOfCat):
    test_list = []
    test_dict = {}
    test_list2 = []
    for each in listOfArt:
        test_list.append(each.split())

    for each in test_list:
        if each[0][0] in listOfCat:
            #print(f"({each[0][0]} : {each[1]})")
            if each[0][0] not in test_dict:
                test_dict[each[0][0]] = int(each[1])
            elif each[0][0] in test_dict:
                test_dict[each[0][0]] = str (int((each[1])) + int(test_dict.get(each[0][0])))

        elif each[0][0] not in listOfCat:
            test_dict[each[0][0]] = "0"


    for each in listOfCat:
        if each not in test_dict:
            test_dict[each] = "0"

    for k, v in test_dict.items():
        if k in listOfCat:
            test_list2.append(f"({k} : {v})")
            test_list2.append(" - ")


    final_dict = {}
    for each in listOfCat:
        for k, v in test_dict.items():
            if each == k:
                final_dict[each] = v


    answer = []
    count = 0
    for k, v in final_dict.items():
            answer.append(f"({k} : {v})")
            answer.append(" - ")
            count += int(v)

    if count == 0:
        return ""


    return "".join(answer[:-1])

