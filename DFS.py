from image_processing import image_to_matrix

# Import the maze matrix obtained from image processing
maze = image_to_matrix("smallMaze.gif")
initial = (0, 0)
target = (108,209)

def dfs(maze, initial, target):
    stack = [initial]
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited[initial[0]][initial[1]] = True
    parent = {}
    while stack:
        current = stack.pop()
        if current == target:
            path = []
            while current in parent:
                path.insert(0, current)
                current = parent[current][0]
            path.insert(0, initial)
            return path
        x, y = current
        neighbors = [(x - 1, y, "north"), (x + 1, y, "south"), (x, y - 1, "west"), (x, y + 1, "east")]
        for neighbor_x, neighbor_y, direction in neighbors:
            if 0 <= neighbor_x < len(maze) and 0 <= neighbor_y < len(maze[0]) and maze[neighbor_x][
                neighbor_y] == 1 and not visited[neighbor_x][neighbor_y]:
                stack.append((neighbor_x, neighbor_y))
                visited[neighbor_x][neighbor_y] = True
                parent[(neighbor_x, neighbor_y)] = current, direction
    return None


path = dfs(maze, initial, target)
if path:
    # print("Coordinates:", path)
    print("Target Position:", path[-1])
else:
    print("No path found.")
states = dfs(maze, initial, target)
