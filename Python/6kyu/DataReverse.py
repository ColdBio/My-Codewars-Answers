"""
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.
"""
def data_reverse(data):
    store_1 = []
    place_holder_value = 0
    for each in range(0, len(data)+4, 8):
        #print(x[test:each])
        store_1.append(data[place_holder_value:each])
        place_holder_value  = each
    
    store_2 = store_1[::-1]
    answer = []

    for each in store_2:
        answer += each

    return answer
