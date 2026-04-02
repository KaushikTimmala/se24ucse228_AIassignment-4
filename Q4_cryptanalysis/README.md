## Crypt-Arithmetic Puzzle using Constraint Satisfaction Problem (CSP)

This project implements a solution to the classic crypt-arithmetic puzzle SEND + MORE = MONEY using Constraint Satisfaction Problem (CSP) techniques. The goal is to assign digits to letters such that the arithmetic equation holds true.

## Objective

The objective of this project is to:
- Solve a crypt-arithmetic puzzle using CSP
- Assign unique digits to each letter
- Ensure all arithmetic constraints are satisfied
- Demonstrate backtracking and constraint checking

## Problem Description

The puzzle is:

    SEND
  + MORE
  -------
   MONEY

Each letter represents a unique digit from 0 to 9. The goal is to find a valid digit assignment such that the equation is numerically correct.

## CSP Formulation

The problem is modeled as a Constraint Satisfaction Problem with the following components:

### Variables
S, E, N, D, M, O, R, Y

### Domains
Each variable can take a value from:
0 to 9

### Constraints
- All letters must have different digits
- Leading digits cannot be zero:
  - S ≠ 0
  - M ≠ 0
- The arithmetic equation must be satisfied:
  SEND + MORE = MONEY

## Approach

The solution uses a backtracking algorithm:
- Assign digits to letters one by one
- Check constraints after each assignment
- If constraints are violated, backtrack
- Continue until a valid solution is found

## Algorithm

1. Start with empty assignment
2. Select an unassigned variable
3. Assign a digit from domain (0–9)
4. Ensure:
   - Digit is not already used
   - Leading digit constraint holds
   - Partial arithmetic constraints are valid
5. Recursively assign next variable
6. If failure occurs, backtrack
7. Stop when all variables are assigned

## Constraint Handling

The program enforces multiple constraints:
- All-different constraint ensures unique digits
- Leading digit constraint avoids invalid numbers
- Partial sum constraints improve efficiency
- Final equation validation ensures correctness

## Data Structures Used

- List to store variables (letters)
- Dictionary for variable assignments
- Dictionary for domains
- Functions for constraint checking

## Execution Steps

1. Install Python (version 3.x)
2. Save the code in a file (e.g., cryptarithmetic.py)
3. Run the program using:
   python cryptarithmetic.py
4. The program will display the solution and verification

## Sample Output

Solution Found:

D = 7  
E = 5  
M = 1  
N = 6  
O = 0  
R = 8  
S = 9  
Y = 2  

Verification:

9567 + 1085 = 10652

## Features

- Solves crypt-arithmetic puzzle using CSP
- Uses backtracking search
- Enforces all constraints effectively
- Includes verification of final result
- Efficient due to partial constraint checking

## Advantages

- Clear demonstration of CSP concepts
- Efficient pruning using constraints
- Works without external libraries
- Can be extended to other puzzles

## Limitations

- Designed for a specific puzzle
- Backtracking may take time for larger problems
- No advanced heuristics like MRV or AC-3

## Future Enhancements

- Implement MRV (Minimum Remaining Values heuristic)
- Add forward checking
- Apply constraint propagation (AC-3)
- Extend to solve multiple crypt-arithmetic puzzles
- Build GUI for interactive solving
- Accept user-defined puzzles

## Applications

- Artificial Intelligence problem solving
- Puzzle solving systems
- Constraint-based reasoning
- Educational demonstrations

## Conclusion

This project demonstrates how crypt-arithmetic puzzles can be solved using Constraint Satisfaction Problem techniques. The use of backtracking and constraint checking ensures that all conditions are satisfied while efficiently finding a valid solution.
