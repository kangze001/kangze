import unittest
from random_walk import RandomWalk

class randomWalkTestCase(unittest.TestCase):
    def test_num_points(self):
       randomwalk = RandomWalk()
       self.assertEqual(5000,randomwalk.num_points)
    
if __name__ == "__main__":
    unittest.main()