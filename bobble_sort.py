"""
Bobble sort
Complexity: n2
"""


def bobble_sort(list_of_elements):
    no_of_items = len(list_of_elements)
    while no_of_items - 1:
        for index in range(no_of_items - 1):
            if list_of_elements[index] > list_of_elements[index + 1]:
                temp = list_of_elements[index]
                list_of_elements[index] = list_of_elements[index + 1]
                list_of_elements[index + 1] = temp

        no_of_items -= 1

if __name__ == '__main__':
    test_list = [12, 4, 453, 56, 22]
    print 'Before sort', test_list
    bobble_sort(test_list)
    print 'After test', test_list

