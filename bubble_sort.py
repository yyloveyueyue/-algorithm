# -*- coding:utf-8 -*-
import copy


def bubble_sort(alist):
    """
    冒泡排序法，2次循环，每次只交换前后两个
    :param alist: 代排序的数组
    :return: 无，内部排序
    """
    for p_num in range(len(alist) - 1 , 0, -1):
        for i in range(p_num):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def bubble_sort_short(alist):
    """
    短冒泡排序，增加额外终止判断，若第一次循环中有一轮并没有发生交换，就提前终止
    :param alist: 代排序的数组
    :return: 无，内部排序
    """
    for p_num in range(len(alist) - 1 , 0, -1):
        exchange = False
        for i in range(p_num):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchange = True
    if not exchange:
        return


def test_of_bubble_sort():
    alist = [23,56,1,10,78,66,36]
    alist_test1 = copy.deepcopy(alist)
    bubble_sort(alist_test1)
    print(alist_test1)
    alist_test2 = copy.deepcopy(alist)
    bubble_sort_short(alist_test2)
    print(alist_test2)

if __name__ == '__main__':
    test_of_bubble_sort()