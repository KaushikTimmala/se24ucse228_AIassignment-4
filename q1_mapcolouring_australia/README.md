# Map Coloring using CSP (Australia)

## Problem Description
This project implements the Map Coloring problem as a Constraint Satisfaction Problem (CSP). The goal is to assign colors to regions of Australia such that no two adjacent regions have the same color.

## Regions (Variables)
- WA (Western Australia)
- NT (Northern Territory)
- Q (Queensland)
- SA (South Australia)
- NSW (New South Wales)
- V (Victoria)
- T (Tasmania)

## Domain (Colors)
- Red
- Green
- Blue

## Constraints
Adjacent regions must not have the same color:

- WA ≠ NT
- WA ≠ SA
- NT ≠ SA
- NT ≠ Q
- SA ≠ Q
- SA ≠ NSW
- SA ≠ V
- Q ≠ NSW
- NSW ≠ V
- T has no adjacent regions

## Approach
The problem is solved using the Backtracking algorithm:

1. Select an unassigned region
2. Assign a color from the domain
3. Check if the assignment satisfies constraints
4. If valid, continue to next region
5. If not, backtrack and try another color

## Algorithm
- Constraint Satisfaction Problem (CSP)
- Backtracking Search

## Code Implementation (Python)
```python
regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]

    return None

solution = backtrack({})

for region in regions:
    print(region, ":", solution[region])
## Sample Output
WA : Red
NT : Green
Q : Red
SA : Blue
NSW : Green
V : Red
T : Red
## Features
- Implements Map Coloring as a Constraint Satisfaction Problem (CSP)
- Uses Backtracking algorithm for finding a valid solution
- Ensures no two adjacent regions share the same color
- Simple and easy-to-understand Python code
- Modular structure (separate validation and solving functions)
- Works with minimal resources (no external libraries required)

## Future Improvements
- Implement MRV (Minimum Remaining Values) heuristic for better efficiency
- Add Forward Checking to reduce search space
- Use Constraint Propagation techniques
- Visualize the map with colored regions (GUI or graph)
- Extend to more complex maps or higher number of colors
- Convert implementation into other languages like C or Java
