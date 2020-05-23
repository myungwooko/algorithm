"""
284. Peeking Iterator
Medium

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache = None
        # 초기에 딱 한번만 이걸로 찝어주는 거니까 그런의미로서 들어온거 그대로.
        self.status = iterator.hasNext()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.cache:
            self.cache = self.iterator.next()
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        if self.cache:
            x = self.cache
            self.cache = None
        else:
            x = self.iterator.next()
        self.status = self.iterator.hasNext()
        return x

    def hasNext(self):
        """
        :rtype: bool
        """
        # simply self.peek애 의해 앞으로 가게 된것은 실제 결과와 관련해서는 안간것으로 count해야 하기 때문에 아래의 로직을 쓴다.
        ##
        # 안간건 안간데로 간건 간데로 정리가 딱 되는게 self.next 이니깐 거기서 행위후 정리를 하게 된 것을 그대로 쓰는 개념.
        # 그러지 않고 그냥 self.iterator.hasNext를 쓰려고 하면 self.peek에서 결과적으로 안간것으로 되어있어야 하는것이 실제로는 한발 나아가 있게 경우에 의해
        # 결과적으로 표현해야 하는 것과 다른 위치를 기준으로 결과를 리턴하게 되는 문제가 따라오게 된다.
        # 그래서 self.next 행위 기준으로 정확하게 정리되어있을때 그것을 self.status에 저장해 놓고 그것을 쓴다.
        return self.status


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

"""
input
["PeekingIterator","next","peek","next","next","hasNext"]
[[[1,2,3]],[],[],[],[],[]] 

output
[null,1,2,2,3,false]
"""