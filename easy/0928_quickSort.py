def quickSort(arr):
    if not arr or len(arr) == 1:
        return arr

    p_idx = len(arr) // 2
    pivot = arr[p_idx]

    s_list = []
    m_list = []
    l_list = []
    for i in arr:
        if i < pivot:
            s_list.append(i)
        elif i == pivot:
            m_list.append(i)
        else:
            l_list.append(i)

    return quickSort(s_list) + m_list + quickSort(l_list)


a = [10,2,3,5,6,4,5,6,67,8]

test = quickSort(a)
print(test)
