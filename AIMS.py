def count_paths(input_string):
    # Parse the input string into a grid
    grid = []
    rows = input_string.split('\n')
    for row in rows:
        cells = row.split()
        grid.append(cells)
    
    # Find the positions of A, B, and x's
    start = None
    end = None
    required_cells = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'A':
                start = (i, j)
                required_cells.add((i, j))
            elif grid[i][j] == 'B':
                end = (i, j)
                required_cells.add((i, j))
            elif grid[i][j] == '.':
                required_cells.add((i, j))
    
    # Check if start or end is missing
    if not start or not end:
        return 0
    
    rows_count = len(grid)
    cols_count = len(grid[0]) if rows_count > 0 else 0
    
    # Check if start or end is on an x (though input validation should prevent this)
    if grid[start[0]][start[1]] == 'x' or grid[end[0]][end[1]] == 'x':
        return 0
    
    total_required = len(required_cells)
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize the count of paths
    path_count = 0
    
    # Visited matrix to track visited positions
    visited = [[False for _ in range(cols_count)] for _ in range(rows_count)]
    visited[start[0]][start[1]] = True  # Mark the start as visited
    
    def dfs(i, j, steps):
        nonlocal path_count
        if (i, j) == end:
            if steps == total_required:
                path_count += 1
            return
        for di, dj in directions:
            ni, nj = i + di, j + dj
            # Check if the new position is within bounds
            if 0 <= ni < rows_count and 0 <= nj < cols_count:
                # Check if the cell is not visited, not an x, and part of required cells
                if not visited[ni][nj] and (ni, nj) in required_cells:
                    visited[ni][nj] = True
                    dfs(ni, nj, steps + 1)
                    visited[ni][nj] = False
    
    # Start DFS from the start position with initial step count 1
    dfs(start[0], start[1], 1)
    
    return path_count


print(count_paths('A x .\n. x .\n. x B'))