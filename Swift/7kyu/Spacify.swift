/*
Modify the spacify function so that it returns the given string with spaces inserted between each character.

spacify("hello world") // "h e l l o   w o r l d"

*/

func spacify(_ str: String) -> String {
    var string = ""
    for each in str {
        string.append(each)
        string.append(" ")
    }
    if str.count > 0 {
        string.removeLast()
    }
    return string
}
