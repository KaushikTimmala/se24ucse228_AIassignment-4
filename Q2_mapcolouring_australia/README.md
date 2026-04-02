## Telangana Map Coloring using CSP

This project implements the Map Coloring problem using Constraint Satisfaction Problem (CSP) techniques for the 33 districts of Telangana. The goal is to assign colors to each district such that no two adjacent districts share the same color.

## Problem Statement

Given 33 districts of Telangana, assign colors to each district in such a way that:
- No two neighboring districts have the same color
- A limited set of colors is used

## Approach

The problem is solved using:
- Backtracking algorithm
- Constraint Satisfaction Problem (CSP)
- Adjacency list representation of districts

Each district is treated as a variable, and colors are assigned while satisfying constraints.

## Technologies Used

- Python
- Basic Data Structures (Lists, Dictionaries)
- Recursion and Backtracking

## Colors Used

The following colors are used:
- Red
- Green
- Blue
- Yellow

## How It Works

1. Define all districts
2. Define neighboring districts using an adjacency list
3. Assign colors one by one using backtracking
4. Check constraints before assigning a color
5. If conflict occurs, backtrack and try another color

## Sample Output

Telangana Map Coloring Solution:

Adilabad -> Red  
Bhadradri_Kothagudem -> Green  
Hyderabad -> Blue  
Jagtial -> Red  
Jangaon -> Green  
Jayashankar_Bhupalpally -> Blue  
Jogulamba_Gadwal -> Yellow  
Kamareddy -> Red  
Karimnagar -> Green  

## Features

- Solves map coloring using CSP
- Uses backtracking for constraint satisfaction
- Ensures no adjacent districts share the same color
- Works for all 33 districts of Telangana

## Future Improvements

- Add full accurate real-world district adjacency
- Implement MRV (Minimum Remaining Values heuristic)
- Add forward checking optimization
- Visualize the colored map using graph plotting libraries
- Convert into GUI or web-based interactive application

## Conclusion

This project demonstrates how CSP and backtracking can be applied to solve real-world problems like map coloring efficiently. It ensures valid color assignments while minimizing conflicts.
