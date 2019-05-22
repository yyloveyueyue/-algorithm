# -*- coding:utf-8 -*-

def insert_sort(alist):
    """
    插入排序，将代插入值插入到已排序数组中的合适位置
    :param alist: 代排序的数组
    :return:
    """
    # todo 分析一下
    for p_num in range(1, len(alist)):
        print(alist)
        cur_val = alist[p_num]
        pos = p_num
        while pos > 0 and alist[pos - 1] > cur_val:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = cur_val



def test_of_insert_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_insert_sort()

