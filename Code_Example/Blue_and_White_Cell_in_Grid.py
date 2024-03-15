# Suppose you have an M x N grid, where each entry represents a cell with a color of either Blue or White. A A white cell will die if it is not connected to other white cells that are touching the border of the grid. Go through the grid and flip the color of white cells that will die to blue.


# 1. Identify the White Cells Connected to the Border: traverse the grid, Depth-First Search (DFS) from every white cell that is on the border. The goal is to mark all white cells connected to the border (either directly or through other white cells) as safe.
# 2. Flip the Color of the Unsafe White Cells: After marking all the safe white cells, we traverse the grid again and flip the color of all white cells that are not marked as safe to blue.



def flip_dying_cells(grid):
   if not grid or not grid[0]:
       return grid
   m, n = len(grid), len(grid[0])
   safe = set()  # Set to keep track of safe cells
   def dfs(x, y):
       """Perform DFS to find all white cells connected to the border."""
       if (x, y) in safe or grid[x][y] == 'Blue':
           return
       safe.add((x, y))
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Directions: up, down, left, right
           nx, ny = x + dx, y + dy
           if 0 <= nx < m and 0 <= ny < n:
               dfs(nx, ny)
   # Start DFS from white cells on the border
   for i in range(m):
       for j in [0, n-1]:  # Left and right borders
           if grid[i][j] == 'White':
               dfs(i, j)
   for j in range(n):
       for i in [0, m-1]:  # Top and bottom borders
           if grid[i][j] == 'White':
               dfs(i, j)
   # Flip the color of unsafe white cells
   for i in range(m):
       for j in range(n):
           if grid[i][j] == 'White' and (i, j) not in safe:
               grid[i][j] = 'Blue'
   return grid
# Example grid
grid = [
   ['Blue', 'White', 'White', 'Blue'],
   ['Blue', 'White', 'Blue', 'Blue'],
   ['Blue', 'Blue', 'Blue', 'Blue'],
   ['Blue', 'White', 'White', 'Blue']
]
# Flip dying cells
result = flip_dying_cells(grid)
for row in result:
   print(row)
