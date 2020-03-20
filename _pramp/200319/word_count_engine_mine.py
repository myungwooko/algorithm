
"""
- case-insensitive
- engine should strip out punctuation
- same occurence case in order exist in the document


1. document => li(document)
2. Counter(doc)
"""
import collections
import re

def word_count_engine(document):
    doc = document.split(" ")
    mapp = {}
    for i, w in enumerate(doc):
        key = (re.sub(r'[^\w\s]', '', w.lower()))
        if key not in mapp:
            mapp[key] = i

    doc = [re.sub(r'[^\w\s]', '', w.lower()) for w in doc]
    cc = collections.Counter(doc)

    res = []
    for k, v in cc.items():
        if k == "":
            continue
        res.append((k, v))

    res.sort(key=lambda x: (-x[1], mapp[x[0]]))
    res = [[i[0], str(i[1])] for i in res]
    return res

input =  "Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. "
test = word_count_engine(input)
print(test)
