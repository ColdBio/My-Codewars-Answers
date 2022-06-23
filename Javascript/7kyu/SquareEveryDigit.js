/*
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
*/

// Time: 873ms | Passed: 103 | Failed: 0
function squareDigits(num){
    let result = "";
    for (let i = 0; i < String(num).length; i++) {
        result += Number(String(num)[i]) ** 2;
    }
    return Number(result);
}

// Example params: squareDigits(3212)
