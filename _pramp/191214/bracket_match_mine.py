import unittest

def bracket_match(text):
    only_right = 0
    left = []
    for c in text:
        if c == "(":
            left.append(c)
        else:
            if left:
                left.pop()
            else:
                only_right += 1
    return len(left) + only_right


"""
Actual = 4
Expected = 0

  "(((((((((((((("      
     ^ 
stack = [(
count = 2
"""

class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(bracket_match("(("), 2)

if __name__ == '__main__':
    unittest.main()

