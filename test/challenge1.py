# Challenge 1 - searching algorithm learning points: linear search, binary search, testing & debugging
# Ada sebuah array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91].
# Carilah posisi dari angka 23 dengan Linear Search dan Binary Search
# Setelah itu buatlah testing dan debugging dalam proses mencari angka tersebut.
# Cover semua positive dan negative test case.


# Linear Search -> mencari target dengan cara memeriksa setiap elemen dalam array satu per satu.
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
        
# Binary Search -> mencari target dengan cara membagi array menjadi dua bagian dan memeriksa bagian yang relevan.
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 23
result1 = linear_search(arr, x)
result2 = binary_search(arr, x)

if result1 != -1:
    print(f"Linear Search: Angka ditemukan di indeks {result1}")
else:
    print("Linear Search: Angka tidak ditemukan di array")
    
if result2 != -1:
    print(f"Binary Search: Angka ditemukan di indeks {result2}")   
else:
    print("Binary Search: Angka tidak ditemukan di array")
