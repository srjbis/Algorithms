"""
Insertion sort
Complexity:
"""


def insertion_sort(list_of_items):
    for index in range(1, len(list_of_items)):
        temp = list_of_items[index]
        position = index

        while position > 0 and list_of_items[position - 1] > temp:
            list_of_items[position] = list_of_items[position - 1]
            position -= 1

        list_of_items[position] = temp

if __name__ == '__main__':
    test_list = [1, 23, 10, 5, 44, 56]
    print 'Before sort: ', test_list
    insertion_sort(test_list)
    print 'After sort: ', test_list
