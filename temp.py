""" quick sort """
def partition(alist, start, end):
    if end <= start:
        return

    # set pivot
    pivot = alist[start]
    left = start + 1
    right = end
    while True:
        while left <= right and alist[left] <= pivot:
            left = left + 1
        while right >= left and alist[right] >= pivot:
            right -= 1

        # right meets left
        if right <= left:
            break

        alist[left], alist[right] = alist[right], alist[left]

    # 中间位置和pivot交换
    alist[right], alist[start] = alist[start], alist[right]

    partition(alist, start, right - 1)
    partition(alist, right + 1, end)


alist = [6,1,2,7,9,3,4,5,10,8]
partition(alist,0,len(alist)-1)
print(alist)