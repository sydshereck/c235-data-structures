'''
    File name: Q1_linear-binary_search.py
    Author: Sydney Shereck
    Student Number: 20207148
    Date: 1/21/2022
    Program: This code compares the runtime complexy of binary search
    and linear search through various test cases.
'''

import time
import random

# Linear Search Algorithm
def linear_search(lst, k):
    n = len(lst)
    # Check each element and compare with target.  
    for i in range(n):
        if lst[i] == k:
            return True
    return False

# Merge Sort Function
def merge (lst1, lst2):
    list_new = []
    pointer_1 = 0
    pointer_2 = 0
    
    while pointer_1 < len(lst1) and pointer_2 < len(lst2):
        if lst1[pointer_1] < lst2[pointer_2]:
            list_new.append(lst1[pointer_1])
            pointer_1 += 1
        else:
            list_new.append(lst2[pointer_2])
            pointer_2 += 1

    while pointer_1 < len(lst1):
        list_new.append(lst1[pointer_1])
        pointer_1 += 1

    while pointer_2 < len(lst2):
        list_new.append(lst2[pointer_2])
        pointer_2 += 1
    return list_new

def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        a_left = merge_sort(a[:len(a)//2])
        a_right = merge_sort(a[len(a)//2:])
        return merge(a_left, a_right)

#Binary Search Algorithm
def binary_search(lst, start, end, k):
    if end >= start:
        mid = (end + start) // 2
        
        # Compare target element with middle element.
        if lst[mid] == k:
            return True
        # If target is smaller than middle, check again in only left sublist.
        elif lst[mid] > k:
            return binary_search(lst, start, mid - 1, k)
        # If target is larger than middle, check again in only right sublist.
        else:
            return binary_search(lst, mid + 1, end, k)

    # Return false is element is not found in list.
    else:
        return False


# Main function
def main():
    S = []
    target_values = []
    n = 1000 # Number of elements in list. 
    k = 10 # Number of target values.

    # Generate search list and target values. 
    for i in range(n):
        S.append(random.randrange(2, 20, 2))
    for j in range(k):
        target_values.append(random.randrange(1, 18))

    # Time how long it takes to conduct linear search.
    start_lin_time = time.time()
    for x in target_values:
        linear_search(S, x)
    end_lin_time = time.time()
    linear_time = end_lin_time - start_lin_time

    # Time how long it takes to sort and conduct binary search.
    start_bin_time = time.time()
    S = merge_sort(S)
    for x in target_values:
        binary_search(S, 0, len(S), x)
    end_bin_time = time.time()
    binary_time = end_bin_time - start_bin_time

    return linear_time, binary_time, n, k

linear_time, binary_time,  n, k = main()
print("It took linear search", round(linear_time, 4), "to search for", k, "items in a list of length", n)
print("It took binary search", round(binary_time, 4), "to search for", k, "items in a list of length", n)
print ("Binary time was faster than linear:", linear_time > binary_time)


















    
