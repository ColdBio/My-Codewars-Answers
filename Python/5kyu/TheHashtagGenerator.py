'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''
def generate_hashtag(s):
    s = s.strip()
    temp_list = []
    result = "#"

    # removing any double spaces
    for each in s.split(" "):
        if each != '':
            temp_list.append(each)
    
    for each in range(0, len(temp_list)):
        if each == '':
            temp_list.remove(each)
        result += temp_list[each][0].upper()
        result += temp_list[each][1:].lower()

    if len(result) > 140 or s == "":
        return False
    else:
        return result
