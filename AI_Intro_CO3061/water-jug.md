# State Space Search: Water Jug Problem

## Problem Description
You are given two jugs, a 4-gallon one and a 3-gallon one, a pump which has unlimited water which you can use to fill the jug, and the ground on which water may be poured. Neither jug has any measuring markings on it. How can you get exactly 2 gallons of water in the 4-gallon jug?

## State Representation
- State: (x, y) where x represents the amount of water in the 4-gallon jug and y represents the amount of water in the 3-gallon jug. 

    Note that 0 ≤ x ≤ 4, and 0 ≤ y ≤ 3 ( x = 0, 1, 2, 3, or 4 and y = 0, 1, 2, 3 )

- Start state: (0, 0)
- Goal state: (2, n) for any n such that n <= 3

>    To solve this we have to make some assumptions not mentioned in the problem:
>
>    - We can fill a jug from the pump.
>    - We can pour water out of a jug to the ground.
>    - We can pour water from one jug to another.
>    - There is no measuring device available.
     

## Operators: 

Define a set of operators that will take us from one state to another.

| Operator | Description |
| -------- | ----------- |
| 1. (x, y) → (4, y) | Fill the 4-gallon jug if x < 4 |
| 2. (x, y) → (x, 3) | Fill the 3-gallon jug if y < 3 |
| 3. (x, y) → (x - d, y) | Pour some water out of the 4-gallon jug if x > 0 |
| 4. (x, y) → (x, y - d) | Pour some water out of the 3-gallon jug if y > 0 |
| 5. (x, y) → (0, y) | Empty the 4-gallon jug on the ground if x > 0 |
| 6. (x, y) → (x, 0) | Empty the 3-gallon jug on the ground if y > 0 |
| 7. (x, y) → (4, y - (4 - x)) | Pour water from the 3-gallon jug into the 4-gallon jug until full if x + y ≥ 4, y > 0 |
| 8. (x, y) → (x - (3 - y), 3) | Pour water from the 4-gallon jug into the 3-gallon jug until full if x + y ≥ 3, x > 0 |
| 9. (x, y) → (x + y, 0) | Pour all the water from the 3-gallon jug into the 4-gallon jug if x + y ≤ 4, y > 0 |
| 10. (x, y) → (0, x + y) | Pour all the water from the 4-gallon jug into the 3-gallon jug if x + y ≤ 3, x > 0 |
| 11. (0, 2) → (2, 0) | Pour 2 gallons from the 3-gallon jug into the 4-gallon jug |
| 12. (2, y) → (0, y) | Empty the 2 gallons in the 4-gallon jug on the ground |


## One Solution Steps
| Gallons in the 3-gallon jug | Gallons in the 4-gallon jug | Rule Applied |
| -------------- | --------------   | ------------ |
| 0              | 0                | 2
| 0              | 3                | 9
| 3              | 0                | 2
| 3              | 3                | 7
| 4              | 2                | 5 or 12
| 0              | 2                | 9 or 11
| 2              | 0                |      --


