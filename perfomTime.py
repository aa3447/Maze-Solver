import time

class MazePerfomTime:
    def __init__(self, maze):
        self.maze = maze
    
    def measure_single_solve_time(self, algorithm):
        start = time.perf_counter()
        self.maze.solve(algorithm)
        end = time.perf_counter()
        print(f"{algorithm} took {end - start:.6f} seconds to solve the maze.")

    def measure_multiple_solve_time(self, algorithm, iterations, sleep_time=0.1):
        total_time = 0
        fastest_time = float("inf")
        slowest_time = float("-inf")
        
        for _ in range(iterations):
            start = time.perf_counter()
            self.maze.solve(algorithm)
            end = time.perf_counter()
            
            elapsed_time = end - start
            fastest_time = min(fastest_time, elapsed_time)
            slowest_time = max(slowest_time, elapsed_time)
            total_time += elapsed_time
            
            self.maze.maze_regenerate()
            time.sleep(sleep_time)  # Optional: sleep to avoid overwhelming the system
        
        print(f"---Report for {algorithm} after {iterations} iterations---")
        print(f"Fastest time: {fastest_time:.6f} seconds")
        print(f"Slowest time: {slowest_time:.6f} seconds")
        print(f"Average time: {total_time / iterations:.6f} seconds")
        print(f"---Report End---")