def search(l, val):
    start = 0
    end = len(l) - 1
    # print(len(l))

    while (end - start) > 1:
        """
        print('Start:', start)
        print('End:', end)
        """
        mid = ((end - start) // 2) + start
        """
        print('Mid:', mid)
        print('//////////////////')
        """
        if l[mid] > val:
            end = mid
        elif l[mid] == val:
            return mid
        else:
            start = mid + 1

    if l[start] == val:
        return start
    elif l[end] == val:
        return end
    else:
        return -1

# def merge_sort(l):