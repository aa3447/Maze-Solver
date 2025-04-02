import unittest
from maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        # This method will run before each test
        self.maze = Maze(0, 0, 5, 5, 10, 10, seed=100)
        self.cells = self.maze.get_cells()
    
    def tearDown(self):
        # This method will run after each test
        self.maze = None
        self.cells = None

    def test_create_cells_rows(self):
        # Test the creation of rows in the maze
        self.assertEqual(len(self.cells), 5)
    
    def test_create_cells_columns(self):
        # Test the creation of columns in the maze
        for row in self.cells:
            self.assertEqual(len(row), 5)
    
    def test_cell_dimensions(self):
        # Test the dimensions of indvidual cells
        for row in self.cells:
            for cell in row:
                self.assertEqual(cell.get_x2() - cell.get_x1(), 10)
                self.assertEqual(cell.get_y2() - cell.get_y1(), 10)
    
    def test_cell_position(self):
        # Test the position of the cells
        for row in range(5):
            for col in range(5):
                cell = self.cells[row][col]
                self.assertEqual(cell.get_x1(), col * 10)
                self.assertEqual(cell.get_y1(), row * 10)
                self.assertEqual(cell.get_x2(), (col + 1) * 10)
                self.assertEqual(cell.get_y2(), (row + 1) * 10)
    
    def test_create_entrance(self):
        # Test the creation of entrance
        entrance_cell = self.cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertTrue(entrance_cell.has_left_wall)

    def test_create_exit(self):
        # Test the creation of exit
        entrance_cell = self.cells[4][4]
        self.assertFalse(entrance_cell.has_bottom_wall)
        self.assertTrue(entrance_cell.has_right_wall)
    
    def test_reset_visited(self):
        # Test the reset of visited cells
        for row in self.cells:
            for cell in row:
                self.assertFalse(cell.visited)


class TestMazeInvalids(unittest.TestCase):
    def test_invalid_cell_width(self):
        # Test invalid cell width
        with self.assertRaises(ValueError):
            Maze(0, 0, 5, 5, -10, 10)

    def test_invalid_cell_height(self):
        # Test invalid cell height
        with self.assertRaises(ValueError):
            Maze(0, 0, 5, 5, 10, -10)

    def test_invalid_num_rows(self):
        # Test invalid number of rows
        with self.assertRaises(ValueError):
            Maze(0, 0, -5, 5, 10, 10)

    def test_invalid_num_cols(self):
        # Test invalid number of columns
        with self.assertRaises(ValueError):
            Maze(0, 0, 5, -5, 10, 10)

    def test_invalid_x1(self):
        # Test invalid x1 coordinate
        with self.assertRaises(ValueError):
            Maze(-1, 0, 5, 5, 10, 10)

    def test_invalid_y1(self):
        # Test invalid y1 coordinate
        with self.assertRaises(ValueError):
            Maze(0, -1, 5, 5, 10, 10)

if __name__ == "__main__":
    unittest.main()