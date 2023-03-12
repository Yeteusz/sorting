def quick_sort(tablica):

    dlugosc = len(tablica)
    if dlugosc <= 1:
        return tablica
    else:
        pivot = tablica.pop()

    liczby_wieksze = []
    liczby_mniejsze = []

    for liczby in tablica:
        if liczby > pivot:
            liczby_wieksze.append(liczby)

        else:
            liczby_mniejsze.append(liczby)

    return quick_sort(liczby_mniejsze) + [pivot] + quick_sort(liczby_wieksze)


tablica = [4, 7, 123, 62, 55, 123, 9, 43, 12]
print(quick_sort(tablica))

