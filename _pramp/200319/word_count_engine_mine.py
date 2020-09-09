"""
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it
and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count,
they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet.
You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

Examples:

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"],
          ["get", "1"], ["by", "1"], ["just", "1"] ]
Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3).
We ask this because in compiled languages such as C#, Java, C++, C etc.,
it’s not straightforward to create mixed-type arrays (as it is, for instance, in scripted languages like JavaScript, Python, Ruby etc.).
The expected output will simply be an array of string arrays.

Constraints:

[time limit] 5000ms
[input] string document
[output] array.array.string
"""

"""
- all unique word
- case insensitive
- return order by ocurrence DESC
- return if same ocurrence, order by existing in the sentence
- output [word, "ocurrence"]
-
"""
"""
- all unique word
- case insensitive
- return order by ocurrence DESC
- return if same ocurrence, order by existing in the sentence
- output [word, "ocurrence"]
-
"""
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


import re
import collections


# Time complexity: O(n*k), n is number of words and k is number of characters for each word
# Space compleity: O(n), ns = words, counted(equal or smaller than n), res(equal or smaller than n) => n + n + n => n
def word_count_engine(document):
    words = document.split(" ")
    words = [re.sub(r'[^a-zA-Z]', '', r).lower() for r in words]
    res = collections.Counter(words).items()
    res.sort(key=lambda x: (-x[1], words.index(x[0])))
    res = [[k, str(v)] for k, v in res if k != ""]
    return res


import string
from collections import Counter

table = string.maketrans("", "")


# Time complexity: O(n^2), *sorted*index
# Space complexity: O(n), *just understood about selecting the biggest one's size
def word_count_engine(document):
    striped = document.lower().translate(table, string.punctuation)
    listing = striped.split(" ")
    counter = Counter(listing).items()
    pre_result = sorted(counter, key=lambda x: (-x[1], listing.index(x[0])))
    return [[pair[0], str(pair[1])] for pair in pre_result if pair[0]]
