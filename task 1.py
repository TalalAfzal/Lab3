from collections import deque


def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([(start, [start])])  # (current position, path taken)
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), path + [(new_x, new_y)]))
                visited.add((new_x, new_y))

    return "No path found"


# Example usage:
grid = [[0] * 5 for _ in range(5)]  # 5x5 grid
start = (1, 1)
end = (4, 4)
print(shortest_path(grid, start, end))
