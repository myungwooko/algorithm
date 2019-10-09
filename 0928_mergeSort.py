class MergeSort:
    def merger(self, left, right):
        result = []
        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    result.append(left[0])
                    left = left[1:]
                else:
                    result.append(right[0])
                    right = right[1:]
            elif len(left) > 0:
                while len(left) > 0:
                    result.append(left[0])
                    left = left[1:]
            else:
                while len(right) > 0:
                    result.append(right[0])
                    right = right[1:]

        return result


    def merge_sort(self, list):
        if len(list) <= 1:
            return list

        mid = len(list) // 2
        left = list[0:mid]
        right = list[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merger(left, right)

m = MergeSort()
test = m.merge_sort([1, 2, 5, 2, 3, 21, 1, 1, 3])
print(test)
