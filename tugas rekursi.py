## LATIHAN 1
# Fungsi untuk membuat struktur menu dari data yang diberikan
def buat_menu(data):
    menu = {}  # Menyimpan setiap menu berdasarkan ID-nya

    # Langkah 1: Buat setiap menu tanpa menghubungkan ke parent dulu
    for id, parent, label in data:
        menu[id] = {'label': label, 'anak': []}  # Setiap menu punya label & daftar anak

    hasil = []  # Menyimpan menu utama (yang parent-nya 0)

    # Langkah 2: Hubungkan menu dengan parent-nya
    for id, parent, _ in data:
        if parent == 0:
            hasil.append(menu[id])  # Jika parent = 0, berarti ini menu utama
        else:
            try:
                menu[parent]['anak'].append(menu[id])  # Masukkan ke dalam daftar anak parent-nya
            except KeyError:
                print(f"⚠️ Kesalahan: Parent dengan ID {parent} tidak ditemukan!")

    return hasil  # Kembalikan struktur menu yang sudah dibuat

# Fungsi untuk mencetak menu dengan format hierarki
def cetak_menu(menu, indent=0):
    for item in menu:
        print(" " * indent + item['label'])  # Cetak nama menu dengan indentasi
        cetak_menu(item['anak'], indent + 4)  # Cetak anak-anaknya dengan indent lebih dalam

# Meminta input jumlah menu dari pengguna
while True:
    try:
        n = int(input("Jumlah menu: "))  # Memastikan input adalah angka
        break
    except ValueError:
        print("⚠️ Masukkan angka yang valid!")

data = []
id_terpakai = set()  # Menyimpan ID yang sudah digunakan

# Meminta input data menu dari pengguna
for _ in range(n):
    while True:
        try:
            id = int(input("ID: "))  # Memastikan ID berupa angka
            if id in id_terpakai:
                print(f"⚠️ ID {id} sudah digunakan! Masukkan ID lain.")
                continue
            break
        except ValueError:
            print("⚠️ ID harus berupa angka!")

    id_terpakai.add(id)  # Simpan ID agar tidak bisa dipakai lagi

    while True:
        try:
            parent = int(input("Parent: "))  # Memastikan parent berupa angka
            break
        except ValueError:
            print("⚠️ Parent harus berupa angka!")

    label = input("Label: ")  # Input nama menu
    data.append((id, parent, label))  # Simpan data menu dalam list

# Menampilkan struktur menu yang sudah dibuat
print("\nStruktur Menu:")
cetak_menu(buat_menu(data))

## LATIHAN 2
def palindrom(b):
    if len(b) <= 1:
        return True  # Jika panjang ≤ 1, otomatis palindrom
    
    elif not b[0].isalpha():
        return palindrom(b[1:])  # Lewati karakter awal jika bukan huruf
    
    elif not b[-1].isalpha():
        return palindrom(b[:-1])  # Lewati karakter akhir jika bukan huruf
    
    elif b[0] == b[-1]:
        return palindrom(b[1:-1])  # Cek bagian dalamnya
    
    return False  # Jika ada ketidaksesuaian, berarti bukan palindrom

a = input("Masukkan Kata: ").lower().replace(" ", "")  # Hilangkan spasi
if palindrom(a):
    print("Palindrom")
else:
    print("Bukan Palindrom")