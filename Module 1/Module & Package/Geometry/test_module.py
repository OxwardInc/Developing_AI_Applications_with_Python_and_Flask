import unittest
from area_of_circle import circle
from area_of_rectangle import rectangle

class TestArea(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(circle(5), 56)

class TestRecta(unittest.TestCase):

    def test2(self):
        self.assertEqual(rectangle(5, 10), 50)

unittest.main()