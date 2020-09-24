class Solution(object):
    """QuickSort, Time: O(n^2)"""
    def quickSort(self, nums, start, end):
        if end <= start:
            return
        i = start + 1
        j = end
        while i <= j:
            while i <= j and nums[i] <= nums[start]:
                i += 1
            while i <= j and nums[j] >= nums[start]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[j] = nums[j], nums[start]
        self.quickSort(nums, start, j - 1)
        self.quickSort(nums, j + 1, end)

    """MergeSort, Time: O(n log(n))"""
    """
    그냥 반 잘라서 하는게 아니라 이렇게 하는 이유? 그냥 반자른건 sorting 안되어있는 건 마찬가지자나 => sorting 이 되어있는것부터 앞을 비교햐서 작은걸 먼저 놓아야 최종적으로 모두 정리가 되니까!
    """

    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

    """HeapSort, Time: O(n log(n))"""

    def heapSort(self, nums):
        def heapify(nums, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and nums[i] < nums[l]:
                largest = l
            if r < n and nums[largest] < nums[r]:
                largest = r
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        n = len(nums)

        for i in range(n, -1, -1):
            heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)


input = [3, 4, 6, 2, 9, 34, 2, 1, -4]
s = Solution()
test_quick = s.quickSort(input, 0, len(input) - 1)
test_merge = s.mergeSort(input)
test_heap = s.heapSort(input)
print(input)
print(input)
print(input)
