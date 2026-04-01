# Map Coloring using CSP (Backtracking)

# Variables
regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

# Domains
colors = ['Red', 'Green', 'Blue']

# Adjacency (constraints)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  # No neighbors
}

# Check if assignment is valid
def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm
def backtrack(assignment):
    if len(assignment) == len(regions):
        return assignment

    # Select unassigned variable
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

# Solve CSP
solution = backtrack({})

# Print solution
print("Solution:")
for region in regions:
    print(region, ":", solution[region])
