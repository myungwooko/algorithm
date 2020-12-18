"""
Flatten a Dictionary
A dictionary is a type of data structure that is supported natively in all major interpreted languages
such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively.
In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer,
boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer,
 a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table
that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).

Example:

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d
the result key would be Key2.c.d.

Constraints:

[time limit] 5000ms
[input] Dictionary dict
[output] Dictionary- value's type is only string, integer, another dictionary
- inner level's dictionary's key has to be concatenated by dot with outer level's key
- empty key -> skip
"""


# Time complexity: O(n), n is number of all values <= but exponential inside*inside*...
# Space complexity: O(n)
def flatten_dictionary(dictionary):
    res = dict()

    def helper(key, value):
        if type(value) == dict:
            for k, v in value.items():
                if not key:
                    next_key = k
                elif not k:
                    next_key = key
                else:
                    next_key = key + "." + k
                helper(next_key, v)
        else:
            res[key] = value
        return

    for k, v in dictionary.items():
        helper(k, v)

    return res


# This solution is righter and better
"""
This solution is not solved by recursion, remember recursion is kind of exponential, 
and everything that can be solved by recursion access can be sloved queue solution. 
And, queue is better than recursion for time complexity.  
"""


# Time complexity: O(n) n is the number of keys of dictionary
# Space complexity: O(m) m is the number of values of dictionary
def flatten_dictionary(dictionary):
    res = dict()
    queue = [(dictionary, "")]
    while queue:
        curr_dic, key_head = queue.pop(0)
        for k, v in curr_dic.items():
            if key_head and k: k = "." + k
            if type(v) == dict:
                queue.append((v, key_head + k))
            else:
                res[key_head + k] = v
    return res


# Time complexity: O(m) m is for number of all keys of argument dictionary.
# Space complexity: O(n) n is for number of all primitive values as value in dictionary.
def flatten_dictionary(dictionary):
    res = dict()
    queue = [(dictionary, "")]
    while queue:
        curr_dict, key_head = queue.pop(0)
        for k, v in curr_dict.items():
            if key_head and k: k = "." + k
            if type(v) == dict:
                queue.append((v, key_head + k))
            else:
                res[key_head + k] = v
    return res


dic = {"Key1": "1", "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": "1"}}}
test = flatten_dictionary(dic)
print(test == {
    'Key1': '1',
    'Key2.a': '2',
    'Key2.b': '3',
    'Key2.c.d': '3',
    'Key2.c.e': '1'
})
