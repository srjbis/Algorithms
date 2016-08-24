"""
Selection sort
Complexity: O(n2)
"""


def selection_sort(list_of_items):
    for index in range(len(list_of_items) - 1, 0, -1):
        max_position = 0
        for location in range(1, index + 1):
            if list_of_items[location] > list_of_items[max_position]:
                max_position = location
        temp = list_of_items[index]
        list_of_items[index] = list_of_items[max_position]
        list_of_items[max_position] = temp

if __name__ == '__main__':
    test_list = [23, 34, 10, 4, 333, 452]
    print 'Before sort: ', test_list
    selection_sort(test_list)
    print 'After sort: ', test_list
