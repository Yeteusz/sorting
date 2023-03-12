def insertion_sort(arr):
    print("Tablica przed sortowaniem: ")
    print(array)
    for i in range(1, (len(arr))):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


array = [4, 7, 123, 62, 55, 123, 9, 43, 12]

insertion_sort(array)
print("Tablica po sortowaniu: ")
print(array)
