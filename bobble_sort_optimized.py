"""
Optimized bobble sort
"""

iteration = 0


def bobble_sort(list_of_elements):
    for index in range(len(list_of_elements) - 1, 0, -1):
        # iterate only up to index for next iteration
        for i in range(index):
            if list_of_elements[i] > list_of_elements[i + 1]:
                # swap element
                temp = list_of_elements[i]
                list_of_elements[i] = list_of_elements[i + 1]
                list_of_elements[i + 1] = temp

if __name__ == '__main__':
    test_list = [12, 1, 34, 444, 56, 122, 555]
    print 'Before sort: ', test_list
    bobble_sort(test_list)
    print 'After sort: ', test_list
