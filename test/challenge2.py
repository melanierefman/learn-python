# Challenge 2: Sorting Algorithm Learning Points: Bubble Sort, Selection Sort, Insertion Sort, Testing & Debugging
# Ada sebuah array: [4, 7, 8, 2, 5, 10, 15, 20, 21, 16, 19].
# Urutkan array tersebut menggunakan Bubble Sort, Selection Sort, dan Insertion Sort.
# Setelah itu buatlah testing dan debugging dalam proses pengurutan array tersebut.
# Cover semua positive dan negative test case.

# Bubble Sort -> mengurutkan array dengan cara membandingkan elemen yang berdekatan dan menukarnya jika berada dalam urutan yang salah.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort -> mengurutkan array dengan cara menemukan elemen terkecil dari array yang belum diurutkan dan menukarnya dengan elemen pertama dari array yang belum diurutkan.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
        
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr = [4, 7, 8, 2, 5, 10, 15, 20, 21, 16, 19]
bubble_sort(arr)
print("Bubble Sort:", arr)
selection_sort(arr)
print("Selection Sort:", arr)
insertion_sort(arr)
print("Insertion Sort:", arr)

