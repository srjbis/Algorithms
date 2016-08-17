"""
Binary search with recursion
"""


def binary_search(alist, find):

    low = 0
    high = len(alist) - 1
    mid = (low + high) // 2
    if high == 0:
        return False

    if find == alist[mid]:
        return True
    elif find > alist[mid]:
        return binary_search(alist[mid + 1:], find)
    else:
        return binary_search(alist[:mid], find)

if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6], 5))
