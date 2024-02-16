import copy
import tkinter as tk
from tkinter import messagebox

class PuzzleGUI:
    def __init__(self, master, start_state, goal_state):
        self.master = master
        self.master.title("8-Puzzle Solver")
        self.master.geometry("300x300")

        self.start_state = start_state
        self.goal_state = goal_state

        self.tiles = []
        self.create_board()

        solve_button = tk.Button(self.master, text="Solve Puzzle", command=self.solve_puzzle)
        solve_button.grid(row=3, column=0, columnspan=3) 

    def create_board(self):
        for i in range(3):
            for j in range(3):
                tile_value = self.start_state[i][j]
                tile_label = tk.Label(self.master, text=str(tile_value) if tile_value is not None else "",
                                    width=5, height=2, relief="solid", borderwidth=1)
                tile_label.grid(row=i, column=j, padx=5, pady=5)
                tile_label.bind("<Button-1>", lambda event, row=i, col=j: self.tile_click(row, col))
                self.tiles.append(tile_label)

    def update_board(self, state):
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                self.tiles[i * 3 + j].config(text=str(value) if value is not None else "")


    def solve_puzzle(self):
        solution = hill_climbing(self.start_state, self.goal_state)
        self.update_board(solution)
        messagebox.showinfo("Solution", "Puzzle solved!")

def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value is not None:
                goal_position = find_position(goal_state, value)
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
    return distance

def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return (i, j)

def generate_successors(state):
    successors = []
    empty_position = find_position(state, None)

    for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_position = (empty_position[0] + move[0], empty_position[1] + move[1])

        if 0 <= new_position[0] < 3 and 0 <= new_position[1] < 3:
            new_state = copy.deepcopy(state)
            new_state[empty_position[0]][empty_position[1]] = state[new_position[0]][new_position[1]]
            new_state[new_position[0]][new_position[1]] = None
            successors.append(new_state)

    return successors

def hill_climbing(start_state, goal_state):
    current_state = copy.deepcopy(start_state)

    while True:
        successors = generate_successors(current_state)
        min_distance = float('inf')
        next_state = None

        for successor in successors:
            distance = manhattan_distance(successor, goal_state)
            if distance < min_distance:
                min_distance = distance
                next_state = successor

        if manhattan_distance(next_state, goal_state) >= manhattan_distance(current_state, goal_state):
            return current_state

        current_state = next_state

if __name__ == "__main__":
    start_state = [
        [2, 8, 3],
        [1, 6, 4],
        [7, None, 5]
    ]

    goal_state = [
        [1, 2, 3],
        [8, None, 4],
        [7, 6, 5]
    ]

    root = tk.Tk()
    puzzle_gui = PuzzleGUI(root, start_state, goal_state)
    root.mainloop()
