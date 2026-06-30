pricelist = {
    "Ayam": 15000,
    "Sapi": 12000,
    "Babi": 10000,
}
nota_items = []
total_kotor = 0.0
total_diskon = 0.0

print("=== KOPERASI MERAH PUTIH ===")
print("Ketik 'cukup' jika Anda telah selesai membeli.")

while True:
    pilihan = input("Masukkan jenis daging (Ayam/Sapi/Babi): ").strip()
    if pilihan.lower() == "cukup":
        break

    jenis = pilihan.capitalize()
    if jenis not in pricelist:
        print("Jenis daging tidak terdaftar. Silakan pilih Ayam, Sapi, atau Babi.")
        continue

    try:
        berat = float(input("Masukkan jumlah kilogram yang dibeli: ").strip())
    except ValueError:
        print("Masukkan angka desimal yang valid untuk kilogram.")
        continue
    if berat <= 0:
        print("Jumlah kilogram harus lebih dari 0.")
        continue

    harga_satuan = pricelist[jenis]
    subtotal = berat * harga_satuan
    diskon = 0.0

    if jenis == "Ayam":
        if berat >= 5:
            diskon = 0.10 * subtotal
    elif jenis == "Sapi":
        if berat >= 2:
            diskon = 0.15 * subtotal
    elif jenis == "Babi":
        if berat >= 3:
            diskon = 0.12 * subtotal

    total_kotor += subtotal
    total_diskon += diskon
    nota_items.append((jenis, berat, harga_satuan, subtotal, diskon))

print("\n=== Nota Pembayaran ===")
if not nota_items:
    print("Tidak ada pembelian. Terima kasih.")
    exit()
print("{:<10} {:>8} {:>14} {:>14} {:>12}".format("Jenis", "Kg", "Harga/kg", "Subtotal", "Diskon"))
print("-" * 64)
for jenis, berat, harga_satuan, subtotal, diskon in nota_items:
    print(
        "{:<10} {:>8.2f} {:>14,} {:>14,} {:>12,}".format(
            jenis,
            berat,
            harga_satuan,
            int(subtotal),
            int(diskon),
        )
    )

total_bersih = total_kotor - total_diskon
print("-" * 64)
print(f"Total Harga               : Rp{int(total_kotor):,}")
print(f"Total Diskon              : Rp{int(total_diskon):,}")
print(f"Total Yang Harus Dibayar  : Rp{int(total_bersih):,}")
print("Terima kasih telah berbelanja di Koperasi Merah Putih!")