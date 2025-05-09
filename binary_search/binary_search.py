import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

if __name__ == "__main__":
    # Create a large list of 1 million elements
    l = list(range(1, 1000001))  # List from 1 to 1,000,000
    target = 999999  # Target value near the end of the list

    # Measure time for naive_search
    start_time = time.time()
    result_naive = naive_search(l, target)
    end_time = time.time()
    print(f"Naive search result: {result_naive}, Time: {end_time - start_time:.6f} seconds")

    # Measure time for binary_search
    start_time = time.time()
    result_binary = binary_search(l, target)
    end_time = time.time()
    print(f"Binary search result: {result_binary}, Time: {end_time - start_time:.6f} seconds")
