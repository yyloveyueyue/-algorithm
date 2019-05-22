# -*- coding:utf-8 -*-


def merge_sort(alist):
    """
    归并排序
    1 递归，不断分成2部分，直到只有一个元素，return；
    2 mid中心，左右2部分，递归调用
    3 遍历左右，将较小值添加
    :param alist:
    :return:
    """
    if len(alist) < 2 :
        return
    mid = len(alist) // 2
    left = alist[:mid]
    right = alist[mid:]
    merge_sort(left)
    merge_sort(right)
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        print(alist)
        if left[i] < right[j]:
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
        k += 1
    if i < len(left):
        alist[k:] = left[i:]
    if j < len(right):
        alist[k:] = right[j:]


def test_of_merge_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_merge_sort()

