import time

class MazePerfomTime:
    def __init__(self, maze):
        self.maze = maze
    
    def measure_single_solve_time(self, algorithm):
        start = time.perf_counter()
        self.maze.solve(algorithm)
        end = time.perf_counter()
        return f"{algorithm} took {end - start:.6f} seconds to solve the maze."

    def measure_multiple_solve_time(self, algorithm, iterations, sleep_time=0.1):
        total_time = 0
        for _ in range(iterations):
            start = time.perf_counter()
            self.maze.solve(algorithm)
            end = time.perf_counter()
            total_time += (end - start)
            self.maze.maze_regenerate()
            time.sleep(sleep_time)  # Optional: sleep to avoid overwhelming the system
        return f"{algorithm} took {total_time / iterations:.6f} seconds on average to solve {iterations} mazes"