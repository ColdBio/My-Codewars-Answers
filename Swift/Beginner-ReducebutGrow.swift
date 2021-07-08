/*
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
*/

func grow(_ arr: [Int]) -> Int {
    var total: Int? = arr[0]
    for each in arr.dropFirst() {
        total! *= each
    }
  return total ?? 0
}
