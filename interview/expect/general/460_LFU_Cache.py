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
        self.k = capacity
        self.cacheFreq = collections.defaultdict(collections.OrderedDict)
        self.cacheKey = {}
        self.leastFreq = 1

    def _evict(self):
        key, _ = self.cacheFreq[self.leastFreq].popitem(last=False)
        del self.cacheKey[key]

    def _update(self, key, new_v=None):
        freq, v = self.cacheKey[key]['freq'], self.cacheKey[key]['value']
        del self.cacheFreq[freq][key]
        if not self.cacheFreq[self.leastFreq]:
            self.leastFreq += 1
        self.cacheKey[key] = {'freq': freq + 1, 'value': new_v or v}
        self.cacheFreq[freq + 1][key] = new_v or v

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cacheKey:
            return -1
        self._update(key)
        return self.cacheKey[key]['value']

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cacheKey:
            self._update(key, value)
            return
        self.cacheKey[key] = {'freq': 1, 'value': value}
        self.cacheFreq[1][key] = value
        if len(self.cacheKey) > self.k:
            self._evict()
        self.leastFreq = 1


# 위 내용 참고
class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int

        *Data structure:
        self.cacheKey  => {key1: {freq: frequency, val: value}...}
        self.cacheFreq => {freq1: [(key, val), ...]...}

        *Algorithm
        simply,
        => key를 통해 해당 frequency를 알수 있다.그것을 통해 cacheFreq에서도 freq 증가 시킬것 시키고 least에 대한 것도 확인 후 정리 진행.
        => 길이가 꽉 찼을때 leastFreq, cacheFreq를 통해 삭제 대상의 key를 얻을수 있다. 그것을 통해 cacheKey 정리,
           확인 후 leastFreq도 정리.

        결국 양방향에서 서로에 대한 정보를 적절히 가지고 있는 것으로 문제 해결.
        """
        self.capacity = capacity
        self.cacheKey = {}
        self.cacheFreq = collections.defaultdict(collections.OrderedDict)
        self.leastFreq = 1

    def get(self, key):
        if key in self.cacheKey:
            freq, val = self.cacheKey[key]["freq"], self.cacheKey[key]["val"]
            self.cacheKey[key]["freq"] = freq + 1
            del self.cacheFreq[freq][key]
            self.cacheFreq[freq + 1][key] = val
            if not self.cacheFreq[self.leastFreq]:
                self.leastFreq += 1
            return val
        return -1

    def put(self, key, val):
        if not self.capacity:
            return
        if self.capacity == len(self.cacheKey) and key not in self.cacheKey:
            outKey, outVal = self.cacheFreq[self.leastFreq].popitem(last=False)
            del self.cacheKey[outKey]
        if key in self.cacheKey:
            freq = self.cacheKey[key]["freq"]
            self.cacheKey[key]["freq"] = freq + 1
            self.cacheKey[key]["val"] = val
            del self.cacheFreq[freq][key]
            self.cacheFreq[freq + 1][key] = val
            if not self.cacheFreq[self.leastFreq]:
                self.leastFreq += 1
        else:
            self.cacheKey[key] = {"freq": 1, "val": val}
            self.leastFreq = 1
            self.cacheFreq[self.leastFreq][key] = val
