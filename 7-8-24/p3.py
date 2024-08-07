#!/usr/bin/env python
# coding: utf-8

# # Problem 3 - Date 7-8-2024

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[24]:


n = 50
workarr = np.random.randint(0,1000,n)
print(len(workarr))
workarr


# In[21]:


# Function to partition the array as per normal quicksort scheme
def partition_left(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

# Function to perform random partition for randomized pivot selection
def partition_right(arr, low, high):
    r = np.random.randint(low, high) # random pivot not necessarily the last element of the array
    arr[r], arr[high] = arr[high], arr[r]
    return partition_left(arr, low, high)


# In[22]:


# Recursive function for quicksort that partitions the array after the pivot is set in the correct position
def quicksort(arr, low, high):
    if low < high:
        p = partition_right(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


# In[23]:


quicksort(workarr, 0, n - 1)
print("Sorted array:")
print(workarr)


# In[ ]:




