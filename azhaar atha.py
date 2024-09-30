print('#Program Menghitung Gaji Karyawan')
print('=================================')

while True:
    jam_kerja=int(input("Masukkan Jam Kerja :"))
    gaji_kerja=float(input("Masukkan Gaji Kerja :"))

    if (jam_kerja > 160):
        gaji_bonus = gaji_kerja + (gaji_kerja * 0.1)
        print("Gaji Asli :", gaji_kerja)
        print("Gaji dengan bonus :", gaji_bonus)
    else:
        print("Gaji Asli :", gaji_kerja)
        print("Tidak ada gaji bonus")

    keluar=input("Apakah ingin keluar dari program? (ya/tidak): ")
    if keluar.lower() == "ya":
        print("Terima kasih telah menggunakan program ini")
        break