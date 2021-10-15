arr = list(map(int, input().split()))

n = len(arr)

"""
In bubble sort adjacent elements are compared and are swapped if they are not in order.

Time complexity:
Best - O(n)
Avg - O(n**2)
Worst  - O(n**2)
"""


for i in range(n):
    for j in range(n - i - 1):  # last i elements are already in place
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
