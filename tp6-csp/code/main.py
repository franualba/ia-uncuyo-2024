import time
from typing import List, Set, Dict
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import pandas as pd

class NQueensSolver:
    def __init__(self, n: int):
        self.n = n
        self.solutions = []
        self.states_explored = 0
    
    def is_safe_backtracking(self, board: List[int], row: int, col: int) -> bool:
        for i in range(row):
            if (board[i] == col or 
                board[i] - i == col - row or 
                board[i] + i == col + row):
                return False
        return True
    
    def solve_backtracking(self) -> List[List[int]]:
        self.solutions = []
        self.states_explored = 0
        board = [-1] * self.n
        
        def backtrack(row: int):
            if row == self.n:
                self.solutions.append(board[:])
                return
            
            for col in range(self.n):
                self.states_explored += 1
                if self.is_safe_backtracking(board, row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1
        
        backtrack(0)
        return self.solutions

    def solve_forward_checking(self) -> List[List[int]]:
        self.solutions = []
        self.states_explored = 0
        
        def initialize_domains() -> List[Set[int]]:
            return [set(range(self.n)) for _ in range(self.n)]
        
        def update_domains(domains: List[Set[int]], row: int, col: int) -> Dict[int, Set[int]]:
            removed = defaultdict(set)
            for future_row in range(row + 1, self.n):
                if col in domains[future_row]:
                    domains[future_row].remove(col)
                    removed[future_row].add(col)
                
                left_diag = col - (future_row - row)
                if left_diag >= 0 and left_diag in domains[future_row]:
                    domains[future_row].remove(left_diag)
                    removed[future_row].add(left_diag)
                
                right_diag = col + (future_row - row)
                if right_diag < self.n and right_diag in domains[future_row]:
                    domains[future_row].remove(right_diag)
                    removed[future_row].add(right_diag)
            
            return removed
        
        def restore_domains(domains: List[Set[int]], removed: Dict[int, Set[int]]):
            for row, cols in removed.items():
                domains[row].update(cols)
        
        def forward_check(row: int, board: List[int], domains: List[Set[int]]):
            if row == self.n:
                self.solutions.append(board[:])
                return
            
            for col in domains[row]:
                self.states_explored += 1
                board[row] = col
                removed = update_domains(domains, row, col)
                
                if all(len(domains[i]) > 0 for i in range(row + 1, self.n)):
                    forward_check(row + 1, board, domains)
                
                restore_domains(domains, removed)
                board[row] = -1
        
        board = [-1] * self.n
        domains = initialize_domains()
        forward_check(0, board, domains)
        return self.solutions

def run_experiment(n: int, num_runs: int = 30):
    results = []
    
    for run in range(num_runs):
        solver = NQueensSolver(n)
        
        # Backtracking
        start_time = time.time()
        solver.solve_backtracking()
        end_time = time.time()
        bt_time = end_time - start_time
        bt_states = solver.states_explored
        
        # Forward Checking
        start_time = time.time()
        solver.solve_forward_checking()
        end_time = time.time()
        fc_time = end_time - start_time
        fc_states = solver.states_explored
        
        results.append({
            'n': n,
            'run': run + 1,
            'backtracking_time': bt_time,
            'backtracking_states': bt_states,
            'forward_checking_time': fc_time,
            'forward_checking_states': fc_states
        })
    
    return results

def plot_results(all_results):
    # Convertir resultados a DataFrame
    df = pd.DataFrame(all_results)
    
    # Crear figura para los boxplots
    plt.figure(figsize=(10, 10))
    
    # Boxplot de tiempos
    plt.subplot(211)
    data_times = []
    labels_times = []
    for n in df['n'].unique():
        n_results = df[df['n'] == n]
        data_times.extend(n_results['backtracking_time'])
        data_times.extend(n_results['forward_checking_time'])
        labels_times.extend([f'BT (n={n})'] * len(n_results))
        labels_times.extend([f'FC (n={n})'] * len(n_results))
    
    sns.boxplot(x=labels_times, y=data_times)
    plt.title('Comparación de Tiempos de Ejecución')
    plt.ylabel('Tiempo (segundos)')
    plt.xticks(rotation=45)
    
    # Boxplot de estados
    plt.subplot(212)
    data_states = []
    labels_states = []
    for n in df['n'].unique():
        n_results = df[df['n'] == n]
        data_states.extend(n_results['backtracking_states'])
        data_states.extend(n_results['forward_checking_states'])
        labels_states.extend([f'BT (n={n})'] * len(n_results))
        labels_states.extend([f'FC (n={n})'] * len(n_results))
    
    sns.boxplot(x=labels_states, y=data_states)
    plt.title('Comparación de Estados Explorados')
    plt.ylabel('Número de Estados')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

def save_results_to_csv(results):
    # Convertir resultados a DataFrame
    df = pd.DataFrame(results)
    
    # Crear nombre de archivo con timestamp
    filename = 'tp6-Nreinas.csv'
    
    # Guardar resultados
    df.to_csv(filename, index=False)
    print(f"Resultados guardados en: {filename}")
    
    # Calcular y mostrar estadísticas
    # print("\nEstadísticas por tamaño de tablero:")
    # for n in df['n'].unique():
    #     n_results = df[df['n'] == n]
    #     print(f"\nResultados para n={n}:")
    #     print("Backtracking:")
    #     print(f"  Media tiempo: {n_results['backtracking_time'].mean():.6f} segundos")
    #     print(f"  Desv. Est. tiempo: {n_results['backtracking_time'].std():.6f} segundos")
    #     print(f"  Media estados: {n_results['backtracking_states'].mean():.2f}")
    #     print(f"  Desv. Est. estados: {n_results['backtracking_states'].std():.2f}")
        
    #     print("Forward Checking:")
    #     print(f"  Media tiempo: {n_results['forward_checking_time'].mean():.6f} segundos")
    #     print(f"  Desv. Est. tiempo: {n_results['forward_checking_time'].std():.6f} segundos")
    #     print(f"  Media estados: {n_results['forward_checking_states'].mean():.2f}")
    #     print(f"  Desv. Est. estados: {n_results['forward_checking_states'].std():.2f}")

# Ejecutar experimentos
all_results = []
for n in [4, 8, 10]:
    results = run_experiment(n)
    all_results.extend(results)

# Guardar resultados en CSV
save_results_to_csv(all_results)

# Mostrar gráficos
plot_results(all_results)