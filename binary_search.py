# -*- coding:utf-8 -*-


def binary_search(alist, item):
    """
    二分查找，非递归
    :param alist: 输入的列表
    :param item: 查找的目标
    :return: 返回查找的索引，若没有查到，返回-1
    """
    start = 0
    end = len(alist) - 1
    while start <= end :
        mid = (start + end) // 2
        if alist[mid] == item:
            return mid
        else:
            if alist[mid] > item:
                end = mid - 1
            else:
                start = mid + 1
    return -1


def binary_search_re(alist, item):
    """
    二分查找，递归模式
    终止条件：传入的数组长度为0
    :param alist: 输入的列表
    :param item: 查找的目标
    :return: 返回查找的索引，若没有查到，返回-1
    """
    if len(alist) == 0:
        return -1
    mid = len(alist) // 2
    if alist[mid] == item:
        return  mid
    else:
        if alist[mid] > item:
            return  binary_search_re(alist[:mid], item)
        else:
            return binary_search_re(alist[mid+1:], item)

def test_binary_search():
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(test_list, 3))
    print(binary_search(test_list, 13))
    print(binary_search_re(test_list, 3))
    print(binary_search_re(test_list, 13))


if __name__ == '__main__':
    test_binary_search()
