nama_program = "Koperasi Merah Putih"
print('---Ayam Murah---')
print('---Dapatkan daging ayam dengan harga murah di Toko Kami---')


def tanya_beli_lagi():
    var_list = ['ya','cukup']
    jawaban = input("Apakah Anda ingin membeli lagi? (ya/cukup): ").strip().lower()
    while jawaban not in var_list:
        jawaban = input("Masukkan 'ya' untuk ya atau 'cukup' untuk tidak: ").strip().lower()
    return jawaban == 'ya'

total_semua_pembelian = 0
jumlah_transaksi = 0

while True:
    Kebutuhan_ayam = float(input("Masukkan kebutuhan ayam (kg):"))
    Harga_ayam = 25000
    Total_harga = int(Kebutuhan_ayam * Harga_ayam)

    print(f'Kebutuhan Ayam :{Kebutuhan_ayam} kg')
    print(f'Total harga yang harus dibayar: Rp{Total_harga:,}')

    if Kebutuhan_ayam > 5:
        print(f'Anda mendapatkan diskon Rp7000')
        Total_harga_diskon = Rp {Total_harga - 7000:,}
    elif Kebutuhan_ayam > 2:
        print(f'Anda mendapatkan diskon Rp5000')
        Total_harga_diskon = Rp {Total_harga - 5000:,}
    else:
        print(f'Tidak ada diskon yang diberikan')
        Total_harga_diskon = Rp {Total_harga:,}

    print(f'Total harga yang harus dibayar: Rp{Total_harga_diskon:,}')

    total_semua_pembelian = Total_harga_diskon
    jumlah_transaksi = 1

    if not tanya_beli_lagi():
        break

print('\nPembelian selesai.')
print(f'Total transaksi             : {jumlah_transaksi} kali')
print(f'Total yang harus dibayarkan : Rp{total_semua_pembelian:,}')