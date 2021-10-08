"""
Linear search is a sequential searching algorithm where we start from one end 
and check every element of the list until the desired element is found.

Time Complexity : O(n)
Space Complexity : O(1)

"""

def linearSearch(arr, item):
    l = len(arr)
    # loops through the array sequentially
    for i in range(l):
        # checks if item is present in array
        if arr[i] == item:
            return f"Element Found at index: {i}"
    return f"Element not found!"

if __name__ == "__main__":
    arr = [2, 5, 3, 8, 34]
    elementToSearch = int(input().strip())
    print(linearSearch(arr, elementToSearch))