print("Ibu memberi perintah, Beli 1 botol susu")
print("Anak menjawab, OK")
print("Anak pergi ke toko")

jumlah_botol_susu = 173
jumlah_telur = 0
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jum;ah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Anak mengecek harganya cukup")
    if jumlah_telur > 0:
        print("Anak membeli 1 botol susu dan 6 butir telur")
    else:
        print("Anak membeli 1 botol susu")
else:
    print("Anak tidak jadi membeli susu")

print("Anak pulang ke rumah")
print("Menyerahkan belanjanya kepada Ibu")