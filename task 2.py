import time

def state_to_tuple(state):
    """string state to a tuple """
    return tuple(tuple(state[i:i+3]) for i in range(0, 9, 3))

def tuple_to_state(matrix):
    """tuple representation back to string """
    return ''.join(''.join(row) for row in matrix)

def get_moves(matrix):

    moves = []
    state = tuple_to_state(matrix)
    index = state.index("0")
    row, col = divmod(index, 3)
    directions = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1)
    }

    for move, (dx, dy) in directions.items():
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            moves.append(state_to_tuple("".join(new_state)))

    return moves

def dfs(start_state, goal_state):

 stack = [(start_state, [])]
 visited = set()

 while stack:
     state, path = stack.pop()
     if state in visited:
         continue

     visited.add(state)

     if state == goal_state:
         return path

     for neighbor in get_moves(state):
         if neighbor not in visited:
             stack.append((neighbor, path + [state]))

 return None


 pass
def main():
    start_state = input("Enter start State: ")
    goal_state = input("Enter goal State: ")
    start_tuple = state_to_tuple(start_state)
    goal_tuple = state_to_tuple(goal_state)

    print("DFS Algorithm")

    start_time = time.time()
    solution_path = dfs(start_tuple, goal_tuple)
    end_time = time.time()
    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path))
        print("No of Nodes Visited:", len(solution_path) + 1)
        for state in solution_path + [goal_tuple]:
            for row in state:
                print(' '.join(row))
            print("-----")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
