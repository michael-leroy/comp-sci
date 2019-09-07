#!/usr/bin/python3


import math
import random

def mergesort(sort_list):
    if len(sort_list) == 1 or len(sort_list) == 0:
        return sort_list[:len(sort_list)]

    middle = math.floor(len(sort_list) / 2)

    left = sort_list[:middle]
    right = sort_list[middle:]

    return merge(mergesort(left), mergesort(right))


def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    #one of the two lists is currently empty.
    #Lets put what is left in...
    for whats_left in left[left_index:]:
        merged.append(whats_left)

    for whats_right in right[right_index:]:
        merged.append(whats_right)
 
    return merged

if __name__ == "__main__":


    #Generate some random lists to test
    random_test = []
    for _ in range(1,10):
        test_data = [random.randint(x,1000) for x in range(1, random.randint(2,11))]
        random_test.append(test_data)

    for random_lists in random_test:
        result = mergesort(random_lists)
        print(result)
        random_lists.sort()
        assert random_lists == result

