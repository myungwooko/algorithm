"""
981. Time Based Key-Value Store
Medium

525

67

Add to List

Share
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"],
       inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"],
       inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]


Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
### First Try => This wasn't passed because of time limit was exceeding

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
"""

"""
if we condider time stamp as a time sequence, we can't get past timestamps value
ex) set ["love","high",10], set ["love","low",20], get ["love",5]
in this case=> get ["love", 5] =>  ""

- data structure
{"key1": {
        "timestamp1": value, 
        "timestamp2": value...
        },  
 "key2": {
        "timestamp1": value...
 }
}

"""
import collections
import bisect

# time limit exceeds
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.db = collections.defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key][timestamp] = value

    # get => one of the largest one for smaller and equal ones
    def get(self, key: str, timestamp: int) -> str:
        ts = self.db[key].keys()
        validTs = [t for t in ts if t <= timestamp]
        if not validTs:
            return ""
        validTs.sort()
        return self.db[key][validTs[-1]]


class TimeMap:

    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)
        return

    # get => one of the largest one for smaller and equal ones
    def get(self, key: str, timestamp: int) -> str:
        # print(1, self.times[key], timestamp)
        i = bisect.bisect(self.times[key], timestamp)

        # in the case of i == 0, return "" bc that means there is no values
        return self.values[key][i - 1] if i else ""



