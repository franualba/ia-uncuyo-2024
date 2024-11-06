import time
import csv
import matplotlib.pyplot as plt
import pandas as pd

class NQueens:
    def __init__(self, size):
        self.size = size
        self.solution = [-1] * size
        self.state_count = 0

    def is_safe(self, row, col):
        for i in range(row):
            if self.solution[i] == col or \
               self.solution[i] - i == col - row or \
               self.solution[i] + i == col + row:
                return False
        return True

    def solve_backtracking(self, row=0):
        if row == self.size:
            return True
        for col in range(self.size):
            self.state_count += 1
            if self.is_safe(row, col):
                self.solution[row] = col
                if self.solve_backtracking(row + 1):
                    return True
                self.solution[row] = -1
        return False

    def solve_forward_checking(self, row=0, available_cols=None):
        if available_cols is None:
            available_cols = [set(range(self.size)) for _ in range(self.size)]
        if row == self.size:
            return True
        for col in available_cols[row].copy():
            self.state_count += 1
            if self.is_safe(row, col):
                self.solution[row] = col
                next_available_cols = [cols.copy() for cols in available_cols]
                for r in range(row + 1, self.size):
                    next_available_cols[r].discard(col)
                    next_available_cols[r].discard(col + (r - row))
                    next_available_cols[r].discard(col - (r - row))
                if self.solve_forward_checking(row + 1, next_available_cols):
                    return True
                self.solution[row] = -1
        return False

def run_experiment(board_size, algorithm):
    total_time = 0
    results = []
    for _ in range(30):
        solver = NQueens(board_size)
        start_time = time.time()
        if algorithm == "BT":
            solver.solve_backtracking()
        elif algorithm == "FC":
            solver.solve_forward_checking()
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
        results.append((elapsed_time, solver.state_count))
    return results

def save_to_csv(data, filename="tp6-Nreinas.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Board Size", "Algorithm", "Iteration", "Time", "States Explored"])
        for board_size, algorithm, iteration, time, states in data:
            writer.writerow([board_size, algorithm, iteration, time, states])

def plot_results(filename="nqueens_results.csv"):
    df = pd.read_csv(filename)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Plot time boxplot
    df_time = df.pivot_table(index="Iteration", columns=["Algorithm", "Board Size"], values="Time")
    df_time.boxplot(ax=ax1)
    ax1.set_title("Time Taken by Algorithm and Board Size")
    ax1.set_ylabel("Time (seconds)")
    #ax1.tick_params(axis='x', rotation=45)

    # Plot states explored boxplot
    df_states = df.pivot_table(index="Iteration", columns=["Algorithm", "Board Size"], values="States Explored")
    df_states.boxplot(ax=ax2)
    ax2.set_title("States Explored by Algorithm and Board Size")
    ax2.set_ylabel("States Explored")
    #ax2.tick_params(axis='x', rotation=45)

    plt.suptitle("N-Queens Problem: Backtracking vs Forward Checking")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def main():
    board_sizes = [4, 8, 10]
    data = []

    for board_size in board_sizes:
        for algorithm in ["BT", "FC"]:
            results = run_experiment(board_size, algorithm)
            for i, (time, states) in enumerate(results):
                data.append((board_size, algorithm, i+1, time, states))

    save_to_csv(data)
    plot_results()

if __name__ == "__main__":
    main()
