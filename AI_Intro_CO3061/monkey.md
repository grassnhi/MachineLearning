# Goal Stack Planning for Monkey and Bananas

## Problem Description:
Consider the following situation: a monkey is in a room. The monkey wants some bananas. There are three locations in the room – locations A, B and C. The monkey is at location A. There is a box in location C. There are some bananas in location B, but they are hanging from the ceiling. The monkey needs to climb up the box to be high enough to take the bananas.

Use the following predicates and actions and apply Goal Stack Planning to generate a plan for the monkey to have the bananas.

### Predicates:
- **At(X)**: the monkey is at location X; 
- **Level(low/high)**: the monkey is at a low/high level;
- **BoxAt(X)**: the box is at location X; 
- **BananasAt(X**): the bananas are at location X;
- **Have(bananas)**: the monkey have the bananas.

### Actions:
- **Move(X, Y)**: the monkey moves from location X to location Y;
- **ClimbUp(X)**: the monkey climbs up the box at location X; 
- **ClimbDown(X)**: the monkey climbs down the box at location X; 
- **MoveBox(X, Y)**: the monkey moves the box from location X to location Y;
- **TakeBananas(X)**: the monkey takes the bananas at location X.

## Specifications for Monkey Actions:

### 1. Move(X, Y):
   - **Precondition:** `At(Monkey, X)`
   - **Add List:** `At(Monkey, Y)`
   - **Delete List:** `At(Monkey, X)`

### 2. ClimbUp(X):
   - **Precondition:** `At(Monkey, X) AND BoxAt(X) AND Level(low)`
   - **Add List:** `Level(high)`
   - **Delete List:** `Level(low)`

### 3. ClimbDown(X):
   - **Precondition:** `At(Monkey, X) AND BoxAt(X) AND Level(high)`
   - **Add List:** `Level(low)`
   - **Delete List:** `Level(high)`

### 4. MoveBox(X, Y):
   - **Precondition:** `At(Monkey, X) AND BoxAt(X)`
   - **Add List:** `BoxAt(Y)`
   - **Delete List:** `BoxAt(X)`

### 5. TakeBananas(X):
   - **Precondition:** `At(Monkey, X) AND BananasAt(X) AND Level(high)`
   - **Add List:** `Have(bananas)`
   - **Delete List:** `BananasAt(X)`

## Goal Stack Planning:

### **Initial State:**
   - `At(Monkey, A)`
   - `Level(low)`
   - `BoxAt(C)`
   - `BananasAt(B)`

### **Goal:**
   - `Take(bananas)`

### Final solution
1. Move(A, C)
2. MoveBox(C, B)
3. ClimbUp(B)
4. TakeBananas(B)
5. Have(bananas)