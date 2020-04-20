
"""
- value's type is only string, integer, another dictionary
- inner level's dictionary's key has to be concatenated by dot with outer level's key
- empty key -> skip
"""
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


# Time: o(N) n is number of all keys
# Space: O(m) m is number of last level values
# didn't use O(1) becuase changing original input is not good habit, as I heard.
def flatten_dictionary(dictionary):
    res = {}

    def helper(path, value):
        if type(value) != dict:
            res[path] = value
            return

        for k, v in value.items():
            if not path:
                helper(k, v)
            elif not k:
                helper(path, v)
            else:
                helper(path + "." + k, v)

    for k, v, in dictionary.items():
        if type(v) is not dict:
            res[k] = v
        else:
            helper(k, v)

    return res


