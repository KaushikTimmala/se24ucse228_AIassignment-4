## Map Coloring using Constraint Satisfaction Problem (CSP)

This project implements the Map Coloring problem using Constraint Satisfaction Problem (CSP) techniques for the regions of Australia. The goal is to assign colors to each region such that no two adjacent regions share the same color.

## Objective

The objective of this project is to:
- Model the map coloring problem as a CSP
- Assign colors to all regions of Australia
- Ensure that no neighboring regions have the same color
- Demonstrate the use of backtracking in solving constraint problems

## Problem Description

The map coloring problem involves coloring a map in such a way that no two adjacent regions have the same color. In this project, the regions of Australia are considered:
WA, NT, Q, SA, NSW, V, T

Each region must be assigned a color while satisfying adjacency constraints.

## CSP Formulation

The problem is represented as a Constraint Satisfaction Problem with the following components:

### Variables
Each region is treated as a variable:
WA, NT, Q, SA, NSW, V, T

### Domains
Each variable can take one of the following colors:
Red, Green, Blue

### Constraints
- Adjacent regions must not have the same color
- Each region must be assigned exactly one color

## Adjacency Representation

The neighboring relationships between regions are defined as:
- WA → NT, SA
- NT → WA, SA, Q
- Q → NT, SA, NSW
- SA → WA, NT, Q, NSW, V
- NSW → Q, SA, V
- V → SA, NSW
- T → No neighbors

## Approach

The solution is implemented using a backtracking algorithm:
- Select an unassigned region
- Try assigning a color from the domain
- Check if the assignment is consistent with constraints
- If valid, proceed recursively
- If not valid, try another color
- If no color works, backtrack

## Algorithm

1. Start with an empty assignment
2. Select an unassigned region
3. Assign a color from the domain
4. Check if assignment is valid:
   - No neighbor has the same color
5. If valid, recursively assign next region
6. If invalid, backtrack and try another color
7. Continue until all regions are assigned

## Data Structures Used

- List to store regions
- Dictionary to store neighbors (adjacency list)
- Dictionary to store domains
- Dictionary to store assignments

## Execution Steps

1. Install Python (3.x recommended)
2. Save the code in a file (e.g., map_coloring.py)
3. Run the program using:
   python map_coloring.py
4. The solution will be displayed on the console

## Sample Output

Solution Found:

WA -> Red  
NT -> Green  
Q -> Red  
SA -> Blue  
NSW -> Green  
V -> Red  
T -> Red  

## Features

- Implements CSP using backtracking
- Uses adjacency constraints effectively
- Simple and modular structure
- Ensures valid color assignment
- Works efficiently for small maps

## Advantages

- Easy to understand and implement
- Demonstrates core CSP concepts
- Requires minimal resources
- Can be extended to larger problems

## Limitations

- Uses basic backtracking without heuristics
- Performance may decrease for large maps
- Does not use advanced constraint propagation

## Future Enhancements

- Implement MRV (Minimum Remaining Values heuristic)
- Add forward checking
- Use AC-3 constraint propagation
- Visualize the map using graph libraries
- Extend to more complex maps like India or Telangana

## Applications

- Geographic map coloring
- Scheduling problems
- Register allocation in compilers
- Resource allocation problems

## Conclusion

This project demonstrates how the map coloring problem can be solved using Constraint Satisfaction Problem techniques. The use of backtracking ensures that all constraints are satisfied while assigning colors efficiently. It serves as a fundamental example of CSP in artificial intelligence.
