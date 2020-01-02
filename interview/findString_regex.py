def test(s, x):
    if not s or not x or len(x) > len(s):
        return -1
    if len(s) < 1 or len(s) > 5*(10**5):
        return -1
    if len(x) < 1 or len(x) > 1000:
        return -1

    if "*" in x:
        x = x.split("*")
        head = x[0]
        tail = x[1]
        for i, v in enumerate(s):
            if s[i:i+len(head)] == head and s[i+len(head)+1:((i+len(head))+1)+len(tail)] == tail:
                return i
    else:
        for i, v in enumerate(s):
            if s[i:i+len(x)] == x:
                return i
    return

#regex
import re
def test_reg(s, x):
    if "*" in x:
        head = r"\b" + re.escape(x[0]) + r"\b"
        tail = r"\b" + re.escape(x[1]) + r"\b"
        star = r'\b[*]\b'
        reg = head + star + tail
    else:
        reg = x
    a = re.search(reg, x)
    if a:
        return a.start()
    return -1


s = "juliasamanthasamanthajulia"
x = "ant*as"

print(test(s,x))









