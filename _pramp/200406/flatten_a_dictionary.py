
"""
- value's type is only string, integer, another dictionary
- inner level's dictionary's key has to be concatenated by dot with outer level's key
- empty key -> skip
"""

def flatten_dictionary1(dictionary):
    d = dictionary
    res = {}

    def helper(value, path):
        if type(value) != dict:
            res[path] = value
            return

        for k, v in value.items():
            if k == "":
                helper(v, path)
            elif path == "":
                helper(v, k)
            else:
                helper(v, path + "." + k)

    for k, v in d.items():
        helper(v, k)

    return res


# Time O(n) * n=numbers of all of keys , Space O(1)
def flatten_dictionary(dictionary):
    d = dictionary

    def helper(value, path):
        if type(value) != dict:
            d[path] = value
            return

        for k, v in value.items():
            if path == "":
                # go to next level directly
                helper(v, k)
            elif k == "":
                # skip the empty string keyt part and keep going
                helper(v, path)
            else:
                # doing normal case
                helper(v, path + "." + k)

    for k, v in d.items():
        # value is dict case we do our helper funciton and have to delete it from original level because it will be added from the last after doing things.
        if type(v) == dict:
            helper(v, k)
            del d[k]
        # not dict case just is remained as it was\
    return d

