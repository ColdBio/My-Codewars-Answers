'''
Create a function that takes a string and separates it into a sequence of letters.

The array will be formatted as so:

[['J','L','L','M']
,['u','i','i','a']
,['s','v','f','n']
,['t','e','e','']]
The function should separate each word into individual letters, with the first word in the sentence having its letters in the 0th index of each 2nd dimension array, and so on.

Shorter words will have an empty string in the place once the word has already been mapped out. (See the last element in the last part of the array.)

Examples:

sep_str("Just Live Life Man")
# => [['J','L','L','M'],
# => ['u','i','i','a'],
# => ['s','v','f','n'],
# => ['t','e','e','']]);

sep_str("The Mitochondria is the powerhouse of the cell")
# => [ [ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
# => [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
# => [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
# => [ '', 'o', '', '', 'e', '', '', 'l' ],
# => [ '', 'c', '', '', 'r', '', '', '' ],
# => [ '', 'h', '', '', 'h', '', '', '' ],
# => [ '', 'o', '', '', 'o', '', '', '' ],
# => [ '', 'n', '', '', 'u', '', '', '' ],
# => [ '', 'd', '', '', 's', '', '', '' ],
# => [ '', 'r', '', '', 'e', '', '', '' ],
# => [ '', 'i', '', '', '', '', '', '' ],
# => [ '', 'a', '', '', '', '', '', '' ]]
'''
def sep_str(st): 
    indiv_words = []
    max_word_len = 0
    result = []
    i = 0

    for each in st.split(" "):
        indiv_words.append([each])

    num_of_words = len(indiv_words)
    # Find the maxiumum length of the word in indiv_words
    for words in indiv_words:
        if len(words[0]) > max_word_len:
            max_word_len = len(words[0])

    # Split each word into letters
    for each in indiv_words:
        if len(each) < max_word_len:
            each[0] = list(each[0])

    # Make each word the same length as the largest word by appending empty string until
    # while loop is false
    for each in indiv_words:
        while len(each[0]) <= max_word_len - 1:
            each[0].append("")
    
    # Take the first letter of each subarray and append it to a new array
    while i < max_word_len:
        for each in indiv_words:
            result.append(each[0][i])
        i += 1

    # Split the final into a separate array every N element calculated by the number of words
    # in the original splitted input
    output = [result[i:i + num_of_words] for i in range(0, len(result), num_of_words)]

    return output

