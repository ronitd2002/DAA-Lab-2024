# DAA-Lab-2024

Solutions of weekly coding assignments/ labs for the course *Design and Analysis of Algorithms* (DAA) *Lab* conducted by prof [Apurba Das](https://sites.google.com/site/apurbadas348math/home) and prof [Sourav Mukhopadhyay](http://www.facweb.iitkgp.ac.in/~sourav/) of **IIT Kharagpur Maths department** held at Takshashila CIC for the session Autumn 2024-25.

def longest_subarray_divisible_by_k(arr, k):
    remainder_map = {0: -1}  # Stores the first occurrence index of each remainder
    max_length = 0
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num
        remainder = current_sum % k

        if remainder < 0:  # To handle negative remainders
            remainder += k

        if remainder in remainder_map:
            max_length = max(max_length, i - remainder_map[remainder])
        else:
            remainder_map[remainder] = i

    return max_length

# Example usage
array = [7, 6, 4, 2, 3, 9]
k = 5
print("Length of the longest subarray:", longest_subarray_divisible_by_k(array, k))




def sliding_window_minimum(A, B):
    n = len(A)
    result = []
    deque = []  # Stores indexes of potential minimums in current window

    for i in range(n):
        # Remove elements that are out of this window
        if deque and deque[0] < i - B + 1:
            deque.pop(0)

        # Remove elements that are greater than the current element
        while deque and A[deque[-1]] > A[i]:
            deque.pop()

        # Add current element at the end of deque
        deque.append(i)

        # If we've hit the window size, add the minimum to result
        if i >= B - 1:
            result.append(A[deque[0]])

    return result

# Example usage
A = [1, 4, 2, 6, -5]
B = 3
print("Minimums of each window:", sliding_window_minimum(A, B))




