/*
Create a function add(n)/Add(n) which returns a function that always adds n to any number

Note for Java: the return type and methods have not been provided to make it a bit more challenging.

addOne = add(1)
addOne(3) // 4
*/

func add(_ n: Int) -> ((Int) -> Int) { 
        return { $0 + n }
}

