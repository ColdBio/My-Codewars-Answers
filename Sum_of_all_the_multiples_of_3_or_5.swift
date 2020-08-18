/*
Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10
*/

func findSum(_ n: Int) -> Int {
    var sum = 0
    for numbers in 1...n {
        if numbers % 3 == 0 || numbers % 5 == 0 {
            sum += numbers
        }
    }
    return sum
}
