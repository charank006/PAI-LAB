import heapq

# Goal state
goal_state = [[1,2,3],[4,5,6],[7,8,0]]

# Directions: up, down, left, right
directions = [(-1,0),(1,0),(0,-1),(0,1)]

def heuristic(state):
    """Manhattan distance heuristic"""
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i = (val-1)//3
                goal_j = (val-1)%3
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_zero(state):
    """Find position of empty tile (0)"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap(state, x1, y1, x2, y2):
    """Swap tiles and return new state"""
    new_state = [row[:] for row in state]
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

def a_star_8_puzzle(start_state):
    """A* search algorithm"""
    visited = set()
    pq = []

    # (f, g, state, path)
    heapq.heappush(pq, (heuristic(start_state), 0, start_state, []))

    while pq:
        f, g, state, path = heapq.heappop(pq)

        state_tuple = tuple(tuple(row) for row in state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        path = path + [state]

        # Goal check
        if state == goal_state:
            return path

        x0, y0 = get_zero(state)

        for dx, dy in directions:
            nx, ny = x0 + dx, y0 + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = swap(state, x0, y0, nx, ny)
                new_state_tuple = tuple(tuple(row) for row in new_state)

                if new_state_tuple not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(new_state)
                    heapq.heappush(pq, (new_f, new_g, new_state, path))

    return None


# Example start state
start_state = [
    [1,2,3],
    [4,0,6],
    [7,5,8]
]

solution = a_star_8_puzzle(start_state)

if solution:
    print(f"Solution found in {len(solution)-1} moves:\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")