"""
- all unique word
- case insensitive
- return order by ocurrence DESC
- return if same ocurrence, order by existing in the sentence
- output [word, "ocurrence"]
-
"""
import re
from collections import Counter


def word_count_engine(document):
    raw_words = document.split(" ")
    words = [(re.sub(r'\W+', '', raw_word)).lower() for raw_word in raw_words]
    mapp = {}
    # word indexing
    for i, word in enumerate(words):
        if word not in mapp:
            mapp[word] = i
    count = Counter(words)
    count = [[k, str(v)] for k, v in count.items() if k != ""]
    # Using mapp[x[0]], it is ordered by index as well
    res = sorted(count, key=lambda x: (-int(x[1]), mapp[x[0]]))
    return res

input =  "Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. "
test = word_count_engine(input)
print(test)
