arr = [4, 7, 123, 62, 55, 123, 9, 43, 12]
print("Tablica przed sortowaniem: ")
print(arr)

for i in range(len(arr)):
    min_id = i

    for j in range(i + 1, len(arr)):
        if arr[min_id] > arr[j]:
            min_id = j
    arr[i], arr[min_id] = arr[min_id], arr[i]
print("Tablica po sortowaniu: ")
print(arr)
