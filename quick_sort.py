# -*- coding:utf-8 -*-

# 方法1
def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quick_sort(arr, left, partitionIndex-1)
        quick_sort(arr, partitionIndex+1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i += 1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# 方法2
def quick_sort_v2(alist, fst, lst):
    """
    快速排序

    :param alist: 待排序列表
    :param fst: 起始idx
    :param lst: 终止idx
    :return: None
    """
    if fst >= lst:
        return
    pivot = alist[fst]
    index = fst + 1
    i = index
    while i <= lst:
        if alist[i] < pivot:
            alist[i], alist[index] = alist[index], alist[i]
            index += 1
            print(alist)
        i += 1
    # p_idx = min(i, j)  # 枢轴索引
    alist[fst], alist[index-1] = alist[index-1], alist[fst]
    print(alist)
    quick_sort_v2(alist, fst, index - 2)
    quick_sort_v2(alist, index, lst)






def test_of_quicj_sort():
    alist = [54, 26, 93, 17, 77, 56, 26, 55, 20]
    # quick_sort(alist)
    print(alist)
    fst1 = 0
    lst1 = len(alist) - 1
    quick_sort_v2(alist,fst1,lst1)
    print(alist)


if __name__ == '__main__':
    test_of_quicj_sort()