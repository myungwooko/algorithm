"""
# if r >= len(pattern) - 1:
  return True
# if same character or character and "." => pass
# if a character and "*"
    # previous character is same => l should move to termination of that char idx
    # else:
        if "previous index of text" and after of "*" of pattern has to be same:
          in that case (l, r + 2)
  return False
"""
"""
# if r >= len(pattern) - 1:
  return True
# if same character or character and "." => pass
# if a character and "*"
    # previous character is same => l should move to termination of that char idx
    # else:
        if "previous index of text" and after of "*" of pattern has to be same:
          in that case (l, r + 2)
  return False
"""


def is_match(text, pattern):
    def helper(l, r):

        # == can be replaced with >= but there will be no more increment after ==
        # == is more concise
        if l == len(text):
            if r == len(pattern):
                return True
            else:
                # case of char* we can eliminate and then can do only next
                if r + 1 < len(pattern) and pattern[r + 1] == "*":
                    return helper(l, r + 2)
                # otherwise(=not char* case)
                else:
                    return False

        # pattern done_with_pramp and text not done_with_pramp
        elif r == len(pattern) and l < len(text):
            return False

        # ('pattern: ', 'ab*d',   'r: ', 1, 'r+2: ', 2)
        # ('text: ',    'abbdbb', 'l: ', 1, 'l+1: ', 2)
        #
        # ('pattern: ', 'a.*d', '  r: ', 1, 'r+2: ', 2)
        # ('text: ',    'abbdbb', 'l: ', 2, 'l+1: ', 3)
        #
        # ('pattern: ', 'ab*d',   'r: ', 1, 'r+2: ', 2)
        # ('text: ',    'abbdbb', 'l: ', 3, 'l+1: ', 4)
        ##################################################
        # pattern next is * case
        elif r + 1 < len(pattern) and pattern[r + 1] == "*":
            if pattern[r] == "." or text[l] == pattern[r]:
                # helper(l+1, r) => use char* multiple chars case <====================================================kind of key to solve for * case
                # helper(l, r+2) => use char* 0 case
                return helper(l, r + 2) or helper(l + 1, r)
            else:
                # should use *char as 0 case
                # ('pattern: ', 'ab*d',   'r: ', 1, 'r+2: ', 2)
                # ('text: ',    'acbdbb', 'l: ', 3, 'l+1: ', 4)
                return helper(l, r + 2)

        # pattern is "." or same case
        elif pattern[r] == "." or pattern[r] == text[l]:
            return helper(l + 1, r + 1)

        # other cases
        else:
            return False

    return helper(0, 0)


def is_match(text, pattern):
    def helper(i, j):
        if i == len(text):
            if j == len(pattern):
                return True
            else:
                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    return helper(i, j + 2)
                else:
                    return False
        elif j == len(pattern) and i < len(text):
            return False
        elif j + 1 < len(pattern) and pattern[j + 1] == "*":
            if text[i] == pattern[j] or pattern[j] == ".":
                return helper(i + 1, j) or helper(i, j + 2)
            else:
                return helper(i, j + 2)
        elif text[i] == pattern[j] or pattern[j] == ".":
            return helper(i + 1, j + 1)
        else:
            return False

    return helper(0, 0)
