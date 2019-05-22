# -*- coding:utf-8 -*-


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
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def test_of_quicj_sort():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist)
    print(alist)


if __name__ == '__main__':
    test_of_quicj_sort()