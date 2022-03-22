#!/bin/bash
:'
You are given a method called main, make it print the line Hello World!, (yes, that includes a new line character at the end) and dont return anything

Note that for some languages, the function main is the entry point of the program.

Heres how it will be tested:

    java Solution.class parameter1 parameter2
Hints:

Check your references
Think about the scope of your method
For prolog you can use write but there are better ways
If you still dont get it probably you can define main as an attribute of the Solution class that accepts a single argument, and that only prints "Hello World!" without any return.
'

#!/bin/bash
function Solution
{
    function main
    {
        echo "Hello World!"
        echo
    }
    main
}
Solution
