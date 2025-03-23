def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for k in range(0, n-i-1):
            if data[k] > data[k+1]:
                data[k], data[k+1] = data[k+1], data[k]

angka = [29, 10, 14, 37, 13, 25, 50]
bubble_sort(angka)
print("Data setelah diurutkan:", angka)