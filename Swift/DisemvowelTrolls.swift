/*
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
*/

func disemvowel(_ s: String) -> String {
    var inputArray = Array(s)
    var result = ""
    
    for letter in 0...inputArray.count - 1{
        if  inputArray[letter] == "a" ||
            inputArray[letter] == "e" ||
            inputArray[letter] == "i" ||
            inputArray[letter] == "o" ||
            inputArray[letter] == "u" ||
            inputArray[letter] == "A" ||
            inputArray[letter] == "E" ||
            inputArray[letter] == "I" ||
            inputArray[letter] == "O" ||
            inputArray[letter] == "U" {
            continue
        }
        result += "\(inputArray[letter])"
        
    }
    return result
}
