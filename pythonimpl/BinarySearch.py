def binary_search(arr, target):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + (hi - lo) // 2)
        v = arr[mid]
        if v == target:
            return True
        elif v < target:
            lo = mid + 1
        else:
            hi = mid
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(binary_search(arr, 3))
    print(binary_search(arr, 7))
    
    