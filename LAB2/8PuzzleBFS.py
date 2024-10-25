from collections import deque

class PuzzleState:
    def __init__(self, board, empty_tile_pos, previous_state):
        self.board = board
        self.empty_tile_pos = empty_tile_pos
        self.previous_state = previous_state

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def is_goal(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def get_neighbors(self):
        neighbors = []
        x, y = self.empty_tile_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append((new_board, (new_x, new_y)))

        return neighbors


def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    visited.add(tuple(map(tuple, initial_state.board)))

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal():
            return current_state

        for neighbor, empty_tile_pos in current_state.get_neighbors():
            neighbor_state = PuzzleState(neighbor, empty_tile_pos, current_state)
            neighbor_tuple = tuple(map(tuple, neighbor_state.board))

            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append(neighbor_state)

    return None


def count_inversions(board):
    flat_board = [num for row in board for num in row if num != 0]
    inversions = sum(1 for i in range(len(flat_board)) for j in range(i + 1, len(flat_board)) if flat_board[i] > flat_board[j])
    return inversions


def is_solvable(board):
    inversions = count_inversions(board)
    return inversions % 2 == 0


def get_initial_board():
    print("Enter the 8-puzzle board (0 for empty tile):")
    board = []
    for i in range(3):
        while True:
            try:
                row = input(f"Enter row {i + 1} (3 numbers separated by spaces): ")
                row_numbers = list(map(int, row.split()))
                if len(row_numbers) != 3 or any(num < 0 or num > 8 for num in row_numbers):
                    raise ValueError
                board.append(row_numbers)
                break
            except ValueError:
                print("Invalid input. Please enter 3 numbers between 0 and 8.")
    return board


def main():
    initial_board = get_initial_board()

    if not is_solvable(initial_board):
        print("This puzzle configuration is not solvable.")
        return

    empty_tile_pos = next((i, row.index(0)) for i, row in enumerate(initial_board) if 0 in row)
    
    initial_state = PuzzleState(initial_board, empty_tile_pos, None)
    solution_state = bfs(initial_state)

    if solution_state:
        # Backtrack to print the solution path
        solution_path = []
        while solution_state:
            solution_path.append(solution_state)
            solution_state = solution_state.previous_state

        print("Solution found with the following board states:")
        for state in reversed(solution_path):
            print(state)
            print()  # For better readability
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
