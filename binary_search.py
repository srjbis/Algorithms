"""
Binary search algorithm

"""


def binary_search(find, sorted_list):
    high = len(sorted_list)
    low = 1
    while low <= high:
        mid = low + (high - low) // 2
        if find == sorted_list[mid]:
            return mid
        elif find > sorted_list[mid]:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == '__main__':
    print(binary_search(34, [1, 4, 5, 6, 11, 15, 34, 67]))