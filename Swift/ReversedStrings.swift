/*
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
*/

func reverse(_ str: String) -> String {
    var strArray = Array(str)
    var answer = ""
    for letters in stride(from: str.count - 1, to: -1, by: -1) {
            answer += "\(strArray[letters])"
    }
    return answer
}
