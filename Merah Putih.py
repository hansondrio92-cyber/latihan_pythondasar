import json
from pathlib import Path

DATA_FILE = "Koperasi Merah Putih.json"
MENU_FILE = Path(DATA_FILE)


def load_data(data_file):
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def create_default_menu(data_file):
    default = {
        "Aneka Daging": {
            "Ayam": {"Nama": "Ayam", "Harga_per_kg": 15000},
            "Sapi": {"Nama": "Sapi", "Harga_per_kg": 12000},
            "Babi": {"Nama": "Babi", "Harga_per_kg": 10000},
        }
    }
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(default, f, ensure_ascii=False, indent=2)
    return default


def ensure_menu(data_file):
    data = load_data(data_file)
    if data is None:
        print(f"File {data_file} tidak ditemukan. Membuat menu default...")
        data = create_default_menu(data_file)
    return data


def build_pricelist(data):
    pricelist = {}
    for key, item in data.get("Aneka Daging", {}).items():
        name = item.get("Nama", key)
        price = item.get("Harga_per_kg", 0)
        pricelist[name] = price
    return pricelist


def display_data(data):
    print("=== KOPERASI MERAH PUTIH ===")
    print("=== Daftar Harga Daging ===")
    print("{:<10} {:>14}".format("Jenis", "Harga/kg"))
    print("-" * 30)
    for item in data["Aneka Daging"].values():
        nama = item["Nama"]
        harga_per_kg = item["Harga_per_kg"]
        print("{:<10} {:>14,}".format(nama, harga_per_kg))
    print("-" * 30)


def get_user_input():
    while True:
        pilihan = input("Masukkan jenis daging (Ayam/Sapi/Babi) atau 'cukup' untuk selesai: ").strip()
        if pilihan.lower() == "cukup":
            return None, None
        jenis = pilihan.capitalize()
        if jenis not in ["Ayam", "Sapi", "Babi"]:
            print("Jenis daging tidak terdaftar. Silakan pilih Ayam, Sapi, atau Babi.")
            continue
        try:
            berat = float(input("Masukkan jumlah kilogram yang dibeli: ").strip())
            if berat <= 0:
                print("Jumlah kilogram harus lebih dari 0.")
                continue
            return jenis, berat
        except ValueError:
            print("Masukkan angka desimal yang valid untuk kilogram.")


def calculate_price(jenis, berat, pricelist):
    harga_satuan = pricelist[jenis]
    subtotal = berat * harga_satuan
    diskon = 0.0
    rule = Discount_Rules.get(jenis)
    if rule and berat >= rule["min_kg"]:
        diskon = rule["discount_rate"] * subtotal
    return harga_satuan, subtotal, diskon


def print_nota(nota_items, total_kotor, total_diskon):
    print("\n=== Nota Pembayaran ===")
    if not nota_items:
        print("Tidak ada pembelian. Terima kasih.")
        return
    print("{:<10} {:>8} {:>14} {:>14} {:>12}".format("Jenis", "Kg", "Harga/kg", "Subtotal", "Diskon"))
    print("-" * 64)
    for jenis, berat, harga_satuan, subtotal, diskon in nota_items:
        print(
            "{:<10} {:>8.2f} {:>14,} {:>14,} {:>12,}".format(
                jenis,
                berat,
                int(harga_satuan),
                int(subtotal),
                int(diskon),
            )
        )
    total_bersih = total_kotor - total_diskon
    print("-" * 64)
    print(f"Total Kotor   : Rp{int(total_kotor):,}")
    print(f"Total Diskon  : Rp{int(total_diskon):,}")
    print(f"Total Bersih  : Rp{int(total_bersih):,}")


def run_kasir():
    data = ensure_menu(DATA_FILE)
    pricelist = build_pricelist(data)
    display_data(data)

    nota_items = []
    total_kotor = 0.0
    total_diskon = 0.0

    while True:
        jenis, berat = get_user_input()
        if jenis is None:
            break
        harga_satuan, subtotal, diskon = calculate_price(jenis, berat, pricelist)
        nota_items.append((jenis, berat, harga_satuan, subtotal, diskon))
        total_kotor += subtotal
        total_diskon += diskon
        print(f"Subtotal: Rp{int(subtotal):,}  Diskon: Rp{int(diskon):,}\n")

    print_nota(nota_items, total_kotor, total_diskon)


if __name__ == "__main__":
    run_kasir()
