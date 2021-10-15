"""
Selection sort searches for the minimum element in an array (ascending order) and
places it at the front of the array.

Time Complexity:
Best, Avg, Worst = O(n**2)

"""


def selectionSort(arr):
    l = len(arr)
    for i in range(l - 1):
        # first i elements are already sorted
        for j in range(i + 1, l):
            if arr[i] > arr[j]:
                # swap
                arr[j], arr[i] = arr[i], arr[j]
    return arr


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(selectionSort(arr))
