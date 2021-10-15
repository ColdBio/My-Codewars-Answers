'''
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
'''
def highest_rank(arr):
    # Temporary array
    tmp = {}

    for each in list(arr):
        tmp[each] = list(arr).count(each)

    tmp2 = []
    for k, v in tmp.items():
        largest = max(tmp.values())
        if v == largest:
            print(k)
            tmp2.append(k)

    return sorted(tmp2)[-1]
