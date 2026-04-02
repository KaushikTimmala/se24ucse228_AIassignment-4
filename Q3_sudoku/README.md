## Sudoku Solver using Constraint Satisfaction Problem (CSP)

This project implements a Sudoku puzzle solver using the principles of Constraint Satisfaction Problems (CSP). The solution uses a backtracking algorithm to assign values to each cell while satisfying all Sudoku constraints.

## Objective

The objective of this project is to:
- Solve a 9x9 Sudoku puzzle using CSP techniques
- Ensure all constraints of Sudoku are satisfied
- Demonstrate the use of backtracking in solving constraint-based problems

## Problem Description

Sudoku is a logic-based number puzzle consisting of a 9x9 grid divided into nine 3x3 subgrids. Some cells are pre-filled with numbers, and the goal is to fill the remaining cells such that:
- Each row contains numbers from 1 to 9 without repetition
- Each column contains numbers from 1 to 9 without repetition
- Each 3x3 subgrid contains numbers from 1 to 9 without repetition

## CSP Formulation

The Sudoku problem can be modeled as a Constraint Satisfaction Problem with the following components:

### Variables
Each cell in the 9x9 grid is considered a variable.
Total variables = 81

### Domains
Each variable can take a value from:
1 to 9

### Constraints
- No duplicate values in any row
- No duplicate values in any column
- No duplicate values in any 3x3 subgrid

## Approach

The solution uses a recursive backtracking algorithm:
- Select an unassigned cell
- Try assigning a value from 1 to 9
- Check if the assignment is valid
- If valid, proceed to the next cell
- If not, try another value
- If no value works, backtrack to the previous step

## Algorithm

1. Start with the initial Sudoku grid
2. Find an empty cell
3. Assign a number from 1 to 9
4. Check constraints:
   - Row constraint
   - Column constraint
   - Subgrid constraint
5. If constraints are satisfied, recursively solve the rest of the grid
6. If constraints fail, reset the cell and try another number
7. Continue until the grid is completely filled

## Data Structures Used

- 2D list (9x9) to represent the Sudoku grid
- Functions to check constraints
- Recursion for backtracking

## Execution Steps

1. Install Python (3.x recommended)
2. Copy the code into a file named sudoku.py
3. Run the program using:
   python sudoku.py
4. The program will display the input Sudoku and the solved Sudoku

## Sample Input

5 3 0 0 7 0 0 0 0  
6 0 0 1 9 5 0 0 0  
0 9 8 0 0 0 0 6 0  
8 0 0 0 6 0 0 0 3  
4 0 0 8 0 3 0 0 1  
7 0 0 0 2 0 0 0 6  
0 6 0 0 0 0 2 8 0  
0 0 0 4 1 9 0 0 5  
0 0 0 0 8 0 0 7 9  

## Sample Output

Solved Sudoku:

5 3 4 6 7 8 9 1 2  
6 7 2 1 9 5 3 4 8  
1 9 8 3 4 2 5 6 7  
8 5 9 7 6 1 4 2 3  
4 2 6 8 5 3 7 9 1  
7 1 3 9 2 4 8 5 6  
9 6 1 5 3 7 2 8 4  
2 8 7 4 1 9 6 3 5  
3 4 5 2 8 6 1 7 9  

## Features

- Solves standard 9x9 Sudoku puzzles
- Uses CSP with backtracking
- Ensures all constraints are satisfied
- Simple and readable implementation
- Works for any valid Sudoku input

## Advantages

- Guarantees correct solution if one exists
- Easy to understand algorithm
- Demonstrates core AI concepts
- No external libraries required

## Limitations

- Backtracking can be slow for very complex puzzles
- No advanced heuristics used
- Does not handle invalid input validation extensively

## Future Improvements

- Implement MRV (Minimum Remaining Values heuristic)
- Add forward checking for optimization
- Use constraint propagation (AC-3 algorithm)
- Build a graphical user interface (GUI)
- Allow user input from file or keyboard
- Visualize solving steps

## Applications

- Puzzle solving systems
- Artificial intelligence research
- Constraint-based problem solving
- Game development

## Conclusion

This project demonstrates how Sudoku can be effectively solved using Constraint Satisfaction Problem techniques. The backtracking algorithm systematically explores possible solutions while ensuring all constraints are met, making it a reliable approach for solving Sudoku puzzles.
