from tabulate import tabulate

# Stok awal
stok = [
    {"ID": 1, "Nama Obat": "Paracetamol", "Jumlah": 110, "Harga Satuan": 5000, "Total Harga": 50000},
    {"ID": 2, "Nama Obat": "Amoxicillin", "Jumlah": 17, "Harga Satuan": 13000, "Total Harga": 91000},
    {"ID": 3, "Nama Obat": "Vitamin C", "Jumlah": 115, "Harga Satuan": 3000, "Total Harga": 45000},
    {"ID": 4, "Nama Obat": "Ibuprofen", "Jumlah": 50, "Harga Satuan": 8000, "Total Harga": 40000},
    {"ID": 5, "Nama Obat": "Ciprofloxacin", "Jumlah": 80, "Harga Satuan": 10000, "Total Harga": 80000},
    {"ID": 6, "Nama Obat": "Aspirin", "Jumlah": 60, "Harga Satuan": 4000, "Total Harga": 24000},
    {"ID": 7, "Nama Obat": "Antihistamin", "Jumlah": 25, "Harga Satuan": 7000, "Total Harga": 17500},
    {"ID": 8, "Nama Obat": "Prednisone", "Jumlah": 30, "Harga Satuan": 12000, "Total Harga": 36000},
    {"ID": 9, "Nama Obat": "Loperamide", "Jumlah": 90, "Harga Satuan": 2000, "Total Harga": 18000},
    {"ID": 10, "Nama Obat": "Multivitamin", "Jumlah": 200, "Harga Satuan": 1500, "Total Harga": 300000},
]

recycle_bin =[]
    

# Fungsi validasi input
def validasi_input_alfabet(prompt, jenis="normal"):
    while True:
        inputan = input(prompt)
        if jenis == "normal":
            # Memastikan hanya huruf, angka, dan spasi yang diperbolehkan
            if all(c.isalnum() or c.isspace() for c in inputan) and inputan.strip() != "":
                return inputan
            else:
                print('Inputan harus berupa huruf, angka, atau spasi, dan tidak kosong!')
        elif jenis == "spasi":
            # Memastikan hanya huruf, angka, dan spasi yang diperbolehkan
            if all(c.isalnum() or c.isspace() for c in inputan) and inputan.strip() != "":
                return inputan
            else:
                print('Inputan hanya boleh huruf, angka, dan spasi, serta tidak kosong!')

def validasi_input_angka(prompt, min_value=None, max_value=None):
    while True:
        inputan = input(prompt)
        if inputan.isdigit():
            inputan = int(inputan)
            if (min_value is not None and inputan < min_value) or (max_value is not None and inputan > max_value):
                print(f"Inputan harus antara {min_value} dan {max_value}.")
            else:
                return inputan
        else:
            print('Inputan harus angka!')

# Fungsi untuk menambah data
def tambah_data(stok):
    while True:
        # Cari ID tertinggi yang ada dalam stok
        if stok:
            ID = max(item['ID'] for item in stok) + 1  # ID baru adalah ID tertinggi + 1
        else:
            ID = 1  # Jika stok kosong, ID pertama adalah 1
        print(f"ID yang akan digunakan adalah: {ID}")
        
        # Memanggil fungsi validasi input untuk nama obat yang bisa mengandung spasi
        nama_obat = validasi_input_alfabet('Masukkan nama obat: ', jenis="spasi")
        
        jumlah = validasi_input_angka('Masukkan jumlah (min 1): ', min_value=1)
        harga_satuan = validasi_input_angka('Masukkan harga satuan (min 1): ', min_value=1)
        total_harga = jumlah * harga_satuan
        print(f'Total harga yang dihitung: {total_harga}')
        
        stok.append({'ID': ID, 'Nama Obat': nama_obat, 'Jumlah': jumlah, 'Harga Satuan': harga_satuan, 'Total Harga': total_harga})
        print("Data berhasil ditambahkan!")
        return baca_data(stok)

# Fungsi untuk membaca dan menampilkan data
def baca_data(stok):
    if not stok:
        print("Tidak ada data obat.")
    else:
        headers = ["ID", "Nama Obat", "Jumlah", "Harga Satuan", "Total Harga"]
        table = [[item['ID'], item['Nama Obat'], item['Jumlah'], item['Harga Satuan'], item['Total Harga']] for item in stok]
        print("\nData Obat:")
        print(tabulate(table, headers=headers, tablefmt="grid"))

# Fungsi untuk update stok
def update_data(stok):
    print("\nUpdate Data Obat")
    ID = int(input('Masukkan ID obat yang ingin diupdate: '))
    item_to_update = next((item for item in stok if item['ID'] == ID), None)
    
    if item_to_update:
        print(f"Data saat ini: {item_to_update}")
        print("1. Update Jumlah")
        print("2. Update Harga Satuan")
        print("3. Update Jumlah dan Harga Satuan")
        print("4. Update Stok")
        pilihan = int(input('Pilih data yang ingin diupdate: '))

        if pilihan == 1:
            jumlah_baru = int(input('Masukkan jumlah baru: '))
            item_to_update['Jumlah'] = jumlah_baru
            item_to_update['Total Harga'] = jumlah_baru * item_to_update['Harga Satuan']
            print("Jumlah berhasil diupdate!")

        elif pilihan == 2:
            harga_baru = int(input('Masukkan harga satuan baru: '))
            item_to_update['Harga Satuan'] = harga_baru
            item_to_update['Total Harga'] = item_to_update['Jumlah'] * harga_baru
            print("Harga satuan berhasil diupdate!")

        elif pilihan == 3:
            jumlah_baru = int(input('Masukkan jumlah baru: '))
            harga_baru = int(input('Masukkan harga satuan baru: '))
            item_to_update['Jumlah'] = jumlah_baru
            item_to_update['Harga Satuan'] = harga_baru
            item_to_update['Total Harga'] = jumlah_baru * harga_baru
            print("Jumlah dan harga satuan berhasil diupdate!")

        elif pilihan == 4:
            print("1. Tambah Stok")
            print("2. Kurangi Stok")
            stok_pilihan = int(input('Pilih aksi untuk stok: '))

            if stok_pilihan == 1:
                tambah_stok = int(input('Masukkan jumlah yang ingin ditambah: '))
                item_to_update['Jumlah'] += tambah_stok
                item_to_update['Total Harga'] = item_to_update['Jumlah'] * item_to_update['Harga Satuan']
                print(f"Stok berhasil ditambah! Stok baru: {item_to_update['Jumlah']}")

            elif stok_pilihan == 2:
                kurangi_stok = int(input('Masukkan jumlah yang ingin dikurangi: '))
                if kurangi_stok <= item_to_update['Jumlah']:
                    item_to_update['Jumlah'] -= kurangi_stok
                    item_to_update['Total Harga'] = item_to_update['Jumlah'] * item_to_update['Harga Satuan']
                    print(f"Stok berhasil dikurangi! Stok baru: {item_to_update['Jumlah']}")
                else:
                    print("Stok yang ingin dikurangi melebihi jumlah stok yang tersedia!")

        # Tampilkan data setelah update stok
        baca_data(stok)
    else:
        print(f"ID {ID} tidak ditemukan.")
def delete_data(stok, recycle_bin):
    print("\nHapus Data Obat")
    baca_data(stok)
    ID = validasi_input_angka('Masukkan ID obat yang ingin dihapus: ', min_value=1)
    item_to_delete = next((item for item in stok if item['ID'] == ID), None)
    
    if item_to_delete:
        stok.remove(item_to_delete)
        recycle_bin.append(item_to_delete)
        print(f"Obat dengan ID {ID} berhasil dihapus dan dipindahkan ke recycle bin.")
    else:
        print(f"ID {ID} tidak ditemukan.")
    

# Fungsi utama untuk menampilkan menu dan menjalankan program
def main():
    stok = [
    {"ID": 1, "Nama Obat": "Paracetamol", "Jumlah": 110, "Harga Satuan": 5000, "Total Harga": 50000},
    {"ID": 2, "Nama Obat": "Amoxicillin", "Jumlah": 17, "Harga Satuan": 13000, "Total Harga": 91000},
    {"ID": 3, "Nama Obat": "Vitamin C", "Jumlah": 115, "Harga Satuan": 3000, "Total Harga": 45000},
    {"ID": 4, "Nama Obat": "Ibuprofen", "Jumlah": 50, "Harga Satuan": 8000, "Total Harga": 40000},
    {"ID": 5, "Nama Obat": "Ciprofloxacin", "Jumlah": 80, "Harga Satuan": 10000, "Total Harga": 80000},
    {"ID": 6, "Nama Obat": "Aspirin", "Jumlah": 60, "Harga Satuan": 4000, "Total Harga": 24000},
    {"ID": 7, "Nama Obat": "Antihistamin", "Jumlah": 25, "Harga Satuan": 7000, "Total Harga": 17500},
    {"ID": 8, "Nama Obat": "Prednisone", "Jumlah": 30, "Harga Satuan": 12000, "Total Harga": 36000},
    {"ID": 9, "Nama Obat": "Loperamide", "Jumlah": 90, "Harga Satuan": 2000, "Total Harga": 18000},
    {"ID": 10, "Nama Obat": "Multivitamin", "Jumlah": 200, "Harga Satuan": 1500, "Total Harga": 300000},
]

    while True:
        print('\nMenu:')
        print('1. Tambah Data')
        print('2. Lihat Data')
        print('3. Cari Data')
        print('4. Update Data')
        print('5. Hapus Data')
        print('6. Recycle Bin')
        print('7. Keluar')
        pilihan = validasi_input_angka('Masukkan pilihan: ', min_value=1, max_value=7)

        if pilihan == 1:
            tambah_data(stok)  # Menambahkan data
        elif pilihan == 2:
            baca_data(stok)  # Membaca data
        elif pilihan == 3:
            cari_data(stok)  # Mencari data
        elif pilihan == 4:
            update_data(stok)  # Mengupdate data
        elif pilihan == 5:
            delete_data(stok, recycle_bin)  # Menghapus data
        elif pilihan == 6:
            recycle_bin_menu(recycle_bin, stok)  # Mengelola recycle bin
        elif pilihan == 7:
            print("Keluar dari program...")
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid, coba lagi!")

def recycle_bin_menu(recycle_bin, stok):
    if not recycle_bin:
        print("\nRecycle bin kosong.")
        return

    print("\nRecycle Bin:")
    headers = ["ID", "Nama Obat", "Jumlah", "Harga Satuan", "Total Harga"]
    table = [[item['ID'], item['Nama Obat'], item['Jumlah'], item['Harga Satuan'], item['Total Harga']] for item in recycle_bin]
    print(tabulate(table, headers=headers, tablefmt="grid"))

    print("1. Restore Obat")
    print("2. Hapus Permanen")
    pilihan = validasi_input_angka('Masukkan pilihan: ', min_value=1, max_value=2)

    if pilihan == 1:
        ID = validasi_input_angka('Masukkan ID obat yang ingin di-restore: ', min_value=1)
        item_to_restore = next((item for item in recycle_bin if item['ID'] == ID), None)
        if item_to_restore:
            recycle_bin.remove(item_to_restore)
            stok.append(item_to_restore)
            print(f"Obat dengan ID {ID} berhasil dipulihkan.")
        else:
            print(f"ID {ID} tidak ditemukan di recycle bin.")
    
    elif pilihan == 2:
        ID = validasi_input_angka('Masukkan ID obat yang ingin dihapus permanen: ', min_value=1)
        item_to_delete = next((item for item in recycle_bin if item['ID'] == ID), None)
        if item_to_delete:
            recycle_bin.remove(item_to_delete)
            print(f"Obat dengan ID {ID} berhasil dihapus permanen.")
        else:
            print(f"ID {ID} tidak ditemukan di recycle bin.")

if __name__ == "__main__":
    main()