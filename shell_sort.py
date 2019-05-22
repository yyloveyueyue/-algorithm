# -*- coding:utf-8 -*-

def shell_sort(alist):
    """
    希尔排序
    1 产生一组起始位置s_pos和增量gap
    2 增量每次累除2，s_pos是增量的遍历
    3 增量插入排序，额外传入起始位置和增量
    4 循环条件为大于等于增量，差值为增量
    :param alist: d代排序的数组
    :return: none
    """

    gap = len(alist) // 2
    while gap > 0 :
        for s_pos in range(gap):
            insert_sort_gap(alist, s_pos, gap)
        gap = gap // 2



def insert_sort_gap(alist, s_pos, gap):
    """
    带增量的插入排序，即不是按照12345这样的顺序，而是1,1+gap,1+gap+gap这样的顺序
    :param alist: 代排序的数组
    :param s_pos: 起始位置
    :param gap: 每次的增量
    :return: None
    """

    for i in range(s_pos + gap, len(alist), gap):
        print(alist)
        cul_val = alist[i]
        pos = i
        while pos >= gap and alist[pos - gap] > cul_val:
            alist[pos] = alist[pos - gap]
            pos -= gap
        alist[pos] = cul_val


def test_of_shell_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_shell_sort()

