import unittest
from functions import *

class TestShortestPath(unittest.TestCase):
    def test_shortest_path(self):
        self.assertEqual(
            shortest_path(
                'City1',
                {'City1': {'City2': 3, 'City3': 8},
                'City2': {'City1': 3, 'City3': 4, 'City4': 2},
                'City3': {'City1': 8, 'City2': 4, 'City5': 4},
                'City4': {'City2': 2, 'City5': 1},
                'City5': {'City3': 4, 'City4': 1}}
            ),
            (
            {'City1': 0,
             'City2': 3,
             'City3': 7,
             'City4': 5,
             'City5': 6},
            {'City1': 'City1',
             'City2': 'City1 -> City2',
             'City3': 'City1 -> City2 -> City3',
             'City4': 'City1 -> City2 -> City4',
             'City5': 'City1 -> City2 -> City4 -> City5'}
            )
        )
