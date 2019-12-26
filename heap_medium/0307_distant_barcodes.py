"""
1054. Distant Barcodes
Medium

In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.



Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]


Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """




"""
discuss

#1
Sort bar codes depending on its occurrence.
We put the most frequent on every two positions,(first, third, fifth...)
In this we, we make sure that no two adjacent bar codes are equal.

Python:

    def rearrangeBarcodes(self, packages):
        i, n = 0, len(packages)
        res = [0] * n
        for k, v in collections.Counter(packages).most_common():
            for _ in xrange(v):
                res[i] = k
                i += 2
                if i >= n: i = 1
        return res
Shorter version:

    def rearrangeBarcodes(self, A):
        count = collections.Counter(A)
        A.sort(key=lambda a: (count[a], a))
        A[1::2], A[::2] = A[0:len(A) / 2], A[len(A) / 2:]
        return A
"""