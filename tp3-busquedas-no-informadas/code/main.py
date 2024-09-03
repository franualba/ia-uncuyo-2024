import numpy as np
import gymnasium as gym
from gym.envs.toy_text.frozen_lake import generate_random_map
from queue import Queue, PriorityQueue
import time
import matplotlib.pyplot as plt
from tqdm import tqdm
import csv
import heapq

def generate_random_map_custom(size=8, p=0.8, max_steps=None):
    """
    Generates a random valid map (one that has a path from start to goal)
    :param size: size of each side of the grid
    :param p: probability that a tile is frozen
    :param max_steps: maximum number of steps allowed for the agent
    :return: A random valid map
    """
    valid = False
    
    while not valid:
        m = np.random.choice(['F', 'H'], (size, size), p=[p, 1-p])
        
        # Set start position
        start_pos = (np.random.randint(size), np.random.randint(size))
        m[start_pos] = 'S'
        
        # Set goal position
        while True:
            goal_pos = (np.random.randint(size), np.random.randint(size))
            if goal_pos != start_pos:
                break
        m[goal_pos] = 'G'
        
        valid = np.sum(m == 'S') == 1 and np.sum(m == 'G') == 1
    
    # Convert the map to a list of strings
    desc = ["".join(row) for row in m]
    
    # Create a new environment
    env = gym.make("FrozenLake-v1", desc=desc, is_slippery=False, render_mode='ansi')
    
    # Set the maximum number of steps
    if max_steps is not None:
        env.spec.max_episode_steps = max_steps
    
    return env

def bfs(env, start, goal):
    queue = Queue()
    queue.put((start, []))
    visited = set()
    
    while not queue.empty():
        (state, path) = queue.get()
        
        if state == goal:
            return path, len(visited)
        
        if state not in visited:
            visited.add(state)
            
            for action in range(4):  # 0: LEFT, 1: DOWN, 2: RIGHT, 3: UP
                next_state, _, terminated, truncated, _ = env.step(action)
                #if not (terminated or truncated):
                queue.put((next_state, path + [action]))
                #some, _ = env.reset()
                env.reset()
                env.unwrapped.s = state
                #print(f"{some}, {state}, {next_state}")
    
    return None, len(visited)

def dfs(env, start, goal, depth_limit=None):
    stack = [(start, [])]
    visited = set()
    
    while stack:
        (state, path) = stack.pop()
        
        if state == goal:
            return path, len(visited)
        
        if state not in visited and (depth_limit is None or len(path) < depth_limit):
            visited.add(state)
            
            for action in range(4):  # 0: LEFT, 1: DOWN, 2: RIGHT, 3: UP
                next_state, _, terminated, truncated, _ = env.step(action)
                #if not (terminated or truncated):
                stack.append((next_state, path + [action]))
                env.reset()
                env.unwrapped.s = state
    
    return None, len(visited)

def ucs(env, start, goal, cost_func):
    pq = PriorityQueue()
    pq.put((0, start, []))
    visited = set()
    
    while not pq.empty():
        (cost, state, path) = pq.get()
        
        if state == goal:
            return path, len(visited)
        
        if state not in visited:
            visited.add(state)
            
            for action in range(4):  # 0: LEFT, 1: DOWN, 2: RIGHT, 3: UP
                next_state, _, terminated, truncated, _ = env.step(action)
                #if not (terminated or truncated):
                new_cost = cost + cost_func(action)
                pq.put((new_cost, next_state, path + [action]))
                env.reset()
                env.unwrapped.s = state
    
    return None, len(visited)

def cost_func_1(action):
    return 1

def cost_func_2(action):
    costs = [1, 2, 3, 4]  # LEFT, DOWN, RIGHT, UP
    return costs[action]

def random_search(env, start, goal, max_steps=1000):
    state = start
    path = []
    visited = set()
    
    for _ in range(max_steps):
        visited.add(state)
        if state == goal:
            return path, len(visited)
        
        action = np.random.randint(0, 4)
        next_state, _, terminated, truncated, _ = env.step(action)
        path.append(action)
        
        if terminated or truncated:
            break
        
        state = next_state
    
    return None, len(visited)

def manhattan_distance(state, goal, grid_size):
    state_y, state_x = state // grid_size, state % grid_size
    goal_y, goal_x = goal // grid_size, goal % grid_size
    return abs(state_x - goal_x) + abs(state_y - goal_y)

def astar_search(env, start, goal, grid_size):
    def heuristic(state):
        return manhattan_distance(state, goal, grid_size)
    
    frontier = [(0, start, [])]
    visited = set()
    g_scores = {start: 0}
    
    while frontier:
        _, current, path = heapq.heappop(frontier)
        
        if current == goal:
            return path, len(visited)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for action in range(4):  # 0: LEFT, 1: DOWN, 2: RIGHT, 3: UP
            next_state, _, terminated, truncated, _ = env.step(action)
            # if terminated or truncated:
            # env.reset()
            # env.unwrapped.s = current
            # continue
            
            tentative_g_score = g_scores[current] + 1
            
            if next_state not in g_scores or tentative_g_score < g_scores[next_state]:
                g_scores[next_state] = tentative_g_score
                f_score = tentative_g_score + heuristic(next_state)
                heapq.heappush(frontier, (f_score, next_state, path + [action]))
            
            env.reset()
            env.unwrapped.s = current
    
    return None, len(visited)

def run_search_algorithm(env, algorithm, start, goal, cost_func=None, depth_limit=None, grid_size=None):
    env.reset()
    env.env.s = start
    start_time = time.time()
    
    if algorithm == 'BFS':
        path, explored = bfs(env, start, goal)
    elif algorithm == 'DFS':
        path, explored = dfs(env, start, goal, depth_limit)
    elif algorithm == 'UCS':
        path, explored = ucs(env, start, goal, cost_func)
    elif algorithm == 'Random':
        path, explored = random_search(env, start, goal)
    elif algorithm == 'A*':
        path, explored = astar_search(env, start, goal, grid_size)
    
    end_time = time.time()
    
    if path is not None:
        cost = sum(cost_func(action) for action in path) if cost_func else len(path)
    else:
        cost = float('inf')
    
    return path, explored, cost, end_time - start_time

def run_experiments(num_trials=30, grid_size=100, p_frozen=0.92, max_steps=1000):
    np.random.seed(42)
    
    algorithms = ['BFS', 'DFS', 'DFS_Limited', 'UCS_1', 'UCS_2', 'Random', 'A*']
    results = {alg: {'explored': [], 'cost': [], 'time': [], 'solution_found': []} for alg in algorithms}
    
    csv_data = []

    for env_n in tqdm(range(num_trials)):
        env = generate_random_map_custom(size=grid_size, p=p_frozen, max_steps=max_steps)
        start, _ = env.reset()
        
        # Find the goal state
        desc = env.unwrapped.desc.flatten()
        goal = np.where(desc == b'G')[0][0]
        
        for alg in algorithms:
            if alg == 'BFS':
                path, explored, cost, time_taken = run_search_algorithm(env, 'BFS', start, goal)
            elif alg == 'DFS':
                path, explored, cost, time_taken = run_search_algorithm(env, 'DFS', start, goal)
            elif alg == 'DFS_Limited':
                path, explored, cost, time_taken = run_search_algorithm(env, 'DFS', start, goal, depth_limit=10)
            elif alg == 'UCS_1':
                path, explored, cost, time_taken = run_search_algorithm(env, 'UCS', start, goal, cost_func=cost_func_1)
            elif alg == 'UCS_2':
                path, explored, cost, time_taken = run_search_algorithm(env, 'UCS', start, goal, cost_func=cost_func_2)
            elif alg == 'Random':
                path, explored, cost, time_taken = run_search_algorithm(env, 'Random', start, goal)
            elif alg == 'A*':
                path, explored, cost, time_taken = run_search_algorithm(env, 'A*', start, goal, grid_size=grid_size)
                
            solution_found = path is not None
            results[alg]['explored'].append(explored)
            results[alg]['cost'].append(cost)
            results[alg]['time'].append(time_taken)
            results[alg]['solution_found'].append(solution_found)

            # Calculate cost for scenario 2
            cost_e2 = sum(cost_func_2(action) for action in path) if path else float('inf')

            csv_data.append({
                'algorithm_name': alg,
                'env_n': env_n,
                'states_n': explored,
                'cost_e1': cost,
                'cost_e2': cost_e2,
                'time': time_taken,
                'solution_found': solution_found
            })
    
    # Write results to CSV
    with open('no-informada-results.csv', 'w', newline='') as csvfile:
        fieldnames = ['algorithm_name', 'env_n', 'states_n', 'cost_e1', 'cost_e2', 'time', 'solution_found']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in csv_data:
            writer.writerow(row)

    return results

def plot_results(results):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    for i, metric in enumerate(['explored', 'cost', 'time']):
        data = [results[alg][metric] for alg in results]
        axes[i].boxplot(data, tick_labels=list(results.keys()))
        axes[i].set_title(f'{metric.capitalize()} States')
        axes[i].set_ylabel('Count' if metric == 'explored' else 'Value')
    
    plt.tight_layout()
    plt.show()

# Run experiments
results = run_experiments()

# Plot results
plot_results(results)

# env = generate_random_map_custom(size=10, p=0.92, max_steps=100)
# start, _ = env.reset()
# print(f"Start: {start}")
        
# desc = env.unwrapped.desc.flatten()
# goal = np.where(desc == b'G')[0][0]
# print(f"Goal: {goal}")

# path, explored, cost, time_taken = run_search_algorithm(env, 'BFS', start, goal)
# print(f"Path: {path}")
# print(f"Total states explored: {explored}")
# print(f"Total cost: {cost}")
# print(f"Time taken: {time_taken}")
