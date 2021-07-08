/*
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
*/

func sumMix(_ arr: [Any]) -> Int {
    let arrSize = arr.count - 1
    var sum: Int = 0
    
    for numbers in 0...arrSize {
        if let intValues = arr[numbers] as? Int {
            sum += intValues
        }
        if let strValues = arr[numbers] as? String {
            sum += Int(strValues)!
        }
    }
    return sum
}
