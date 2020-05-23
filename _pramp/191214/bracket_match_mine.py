def bracket_match(text):
    count = 0
    stack = []
    for e in text:
        if e == "(":
            stack.append(e)
        elif e == ")":
            if not stack:
                count += 1
            else:
                stack.pop()
    return len(stack) + count


"""
Actual = 4
Expected = 0

  "(((((((((((((("      
     ^ 
stack = [(
count = 2
"""
