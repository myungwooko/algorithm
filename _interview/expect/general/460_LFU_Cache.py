"""
460. LFU Cache
Hard

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem,
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted.
This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?


Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
import collections


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cacheKey = {}
        self.cacheFreq = collections.defaultdict(collections.OrderedDict)
        self.leastFreq = 1

    def _evict(self):
        key, val = self.cacheFreq[self.leastFreq].popitem(last=False)
        del self.cacheKey[key]
        # 어차피 조회할 freq들은 모두 set 되어있고(그러므로 get, update는 문제 없고)
        # 남은건 무언가가 새로 들어오는 것 뿐인데 그러면 그때 put에서 self.leastFreq = 1해주면 그걸로 만사형통. 모든게 해결

    # concerning update or get
    def _update(self, key, n_val=None):
        val, freq = self.cacheKey[key]["val"], self.cacheKey[key]["freq"]
        del self.cacheFreq[freq][key]
        if not self.cacheFreq[self.leastFreq]:
            self.leastFreq += 1
        self.cacheFreq[freq + 1][key] = n_val or val
        self.cacheKey[key] = {"val": n_val or val, "freq": freq + 1}

    def get(self, key):
        if key not in self.cacheKey:
            return -1
        self._update(key)
        return self.cacheKey[key]["val"]

    def put(self, key, value):
        if not self.capacity:
            return
        if key in self.cacheKey:
            self._update(key, value)
            return
        if self.capacity == len(self.cacheKey):
            self._evict()
        self.leastFreq = 1
        self.cacheKey[key] = {"val": value, "freq": self.leastFreq}
        self.cacheFreq[self.leastFreq][key] = value
        return




