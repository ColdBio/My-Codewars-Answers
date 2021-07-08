/*
Write a function that when given a number >= 0, returns an Array of ascending length subarrays.
pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
*/

func pyramid(_ n: Int) -> [[Int]] {
    if n == 0 {
        return []
    }
    
    let arr = [1]

    if n == 1 {
        return [[1]]
    }
    var result = [[1]]

    for i in 2...n {
        //for j in 1...n {
        result += arr.map { Array(repeating: $0, count: i) }
        //}
    }

    return result
}
