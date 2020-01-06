import unittest

def bracket_match(text):
    stack = []
    count = 0

    for i in text:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                count += 1
    return count + len(stack)

"""
Expected = 2

  "(("      
    ^ 
stack = [(,(]
count = 0

2
"""

class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(bracket_match("(("), 2)

if __name__ == '__main__':
    unittest.main()

