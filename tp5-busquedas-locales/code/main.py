import random
import math
import time
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_random_state(n):
    return [random.randint(0, n-1) for _ in range(n)]

# H function
def calculate_conflicts(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def hill_climbing(n, max_states):
    current_state = generate_random_state(n)
    current_conflicts = calculate_conflicts(current_state)
    states_evaluated = 0
    h_evolution = [current_conflicts]

    while states_evaluated < max_states:
        if current_conflicts == 0:
            return current_state, states_evaluated, h_evolution

        neighbors = get_neighbors(current_state)
        found_better = False

        for neighbor in neighbors:
            states_evaluated += 1
            neighbor_conflicts = calculate_conflicts(neighbor)

            if neighbor_conflicts < current_conflicts:
                current_state = neighbor
                current_conflicts = neighbor_conflicts
                found_better = True
                h_evolution.append(current_conflicts)
                break

        if not found_better:
            return current_state, states_evaluated, h_evolution

    return current_state, states_evaluated, h_evolution

def simulated_annealing(n, max_states, initial_temperature=1000, cooling_rate=0.995):
    current_state = generate_random_state(n)
    current_conflicts = calculate_conflicts(current_state)
    temperature = initial_temperature
    states_evaluated = 0
    h_evolution = [current_conflicts]

    while states_evaluated < max_states:
        if current_conflicts == 0:
            return current_state, states_evaluated, h_evolution

        temperature *= cooling_rate
        new_state = current_state.copy()
        col = random.randint(0, n-1)
        new_state[col] = random.randint(0, n-1)

        states_evaluated += 1
        new_conflicts = calculate_conflicts(new_state)

        if new_conflicts < current_conflicts or random.random() < math.exp((current_conflicts - new_conflicts) / temperature):
            current_state = new_state
            current_conflicts = new_conflicts
            h_evolution.append(current_conflicts)

    return current_state, states_evaluated, h_evolution

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(state, mutation_rate):
    n = len(state)
    for i in range(n):
        if random.random() < mutation_rate:
            state[i] = random.randint(0, n-1)
    return state

def genetic_algorithm(n, max_states, population_size=100, mutation_rate=0.01):
    population = [generate_random_state(n) for _ in range(population_size)]
    states_evaluated = 0
    best_conflicts = float('inf')
    h_evolution = []

    while states_evaluated < max_states:
        fitness_scores = [1 / (calculate_conflicts(state) + 1) for state in population]
        best_conflicts = min(calculate_conflicts(state) for state in population)
        h_evolution.append(best_conflicts)
        
        if best_conflicts == 0:
            best_state = next(state for state in population if calculate_conflicts(state) == 0)
            return best_state, states_evaluated, h_evolution

        states_evaluated += population_size

        new_population = []
        for _ in range(population_size):
            parent1 = random.choices(population, weights=fitness_scores)[0]
            parent2 = random.choices(population, weights=fitness_scores)[0]
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    best_state = min(population, key=calculate_conflicts)
    return best_state, states_evaluated, h_evolution

def run_algorithm(algorithm, n, max_states, runs=30):
    results = []
    for _ in range(runs):
        start_time = time.time()
        solution, states, _ = algorithm(n, max_states)
        end_time = time.time()
        execution_time = end_time - start_time
        conflicts = calculate_conflicts(solution)
        results.append((solution, states, execution_time, conflicts))
    return results

def analyze_results(results):
    optimal_solutions = sum(1 for r in results if r[3] == 0)
    optimal_percentage = (optimal_solutions / len(results)) * 100
    
    states = [r[1] for r in results]
    times = [r[2] for r in results]
    
    avg_states = np.mean(states)
    std_states = np.std(states)
    avg_time = np.mean(times)
    std_time = np.std(times)
    
    return {
        'optimal_percentage': optimal_percentage,
        'avg_states': avg_states,
        'std_states': std_states,
        'avg_time': avg_time,
        'std_time': std_time,
        'states': states,
        'times': times
    }

def save_results_to_csv(results, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Algorithm', 'N', 'Solution', 'States Evaluated', 'Execution Time', 'Conflicts'])
        for alg, n, result_set in results:
            for solution, states, time, conflicts in result_set:
                writer.writerow([alg, n, solution, states, time, conflicts])

def plot_boxplots(data, title, ylabel, filename):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_h_evolution(h_evolution, algorithm_name, n, filename):
    plt.figure(figsize=(12, 6))
    plt.plot(h_evolution, label=algorithm_name)
    plt.title(f'H Function Evolution for N-Queens (N={n})')
    plt.xlabel('States Evaluated')
    plt.ylabel('Number of Conflicts (H)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def main():
    max_states = 10000
    board_sizes = [4, 8, 10]
    algorithms = [
        ('Hill Climbing', hill_climbing),
        ('Simulated Annealing', simulated_annealing),
        ('Genetic Algorithm', genetic_algorithm)
    ]

    all_results = []
    for alg_name, alg_func in algorithms:
        for n in board_sizes:
            results = run_algorithm(alg_func, n, max_states)
            all_results.append((alg_name, n, results))
            
            # analysis = analyze_results(results)
            # print(f"{alg_name} (N={n}):")
            # print(f"  Optimal solutions: {analysis['optimal_percentage']}%")
            # print(f"  Avg states: {analysis['avg_states']} (±{analysis['std_states']})")
            # print(f"  Avg time: {analysis['avg_time']}s (±{analysis['std_time']}s)")

            _, _, h_evol = alg_func(n, max_states)
            #print(f"{alg_name}, {h_evol}")
            plot_h_evolution(h_evol, alg_name, n, f"h_evol_{alg_name}_{n}")

    save_results_to_csv(all_results, 'tp5-Nreinas.csv')

    # Plotting
    for metric in ['states', 'times']:
        data = {f"{alg_name} (N={n})": analysis[metric]
                for alg_name, n, results in all_results
                for analysis in [analyze_results(results)]}
        
        plot_boxplots(data, 
                      f'Distribution of {metric.capitalize()} for N-Queens Problem',
                      'States Evaluated' if metric == 'states' else 'Execution Time (s)',
                      f'n_queens_{metric}_boxplot.png')


if __name__ == "__main__":
    main()