arr = [4, 7, 123, 62, 55, 123, 9, 43, 12]
print("Tablica przed sortowaniem: ")
print(arr)
sorted = False

while not sorted:
    sorted = True
    for i in range(0, (len(arr)-1)):
        if arr[i] > arr[i + 1]:
            sorted = False
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print("Tablica po sortowaniu: ")
print(arr)
