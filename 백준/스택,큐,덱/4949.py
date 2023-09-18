"""
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
"""

import sys

while 1:
    line = sys.stdin.readline().rstrip()

    if line == ".":
        break

    stack = []

    dict = {")": "(", "]": "["}

    result = "yes"

    for char in line:
        if char in "([":
            stack.append(char)

        if char in ")]":
            if len(stack) == 0:
                result = "no"
                break

            else:
                if dict[char] != stack.pop():
                    result = "no"
                    break
    if len(stack) > 0:
        print("no")
    else:
        print(result)
