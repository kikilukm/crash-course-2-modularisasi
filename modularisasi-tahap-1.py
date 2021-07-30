""""
Menghitung luas segitiga
luas_segitiga = alas * tinggi / 2
"""
print('\nmenghitung total luas seitiga dengan tanpa perintah fungsi')

alas = 10
tinggi = 6
luas_segitiga = alas * tinggi // 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nmenghitung total luas seitiga dengan perintah fungsi')


def hitung_luas_segitiga(alas, tinggi):
    total_luas = alas * tinggi / 2
    return total_luas

alas = 10
tinggi = 3

print(f"\nHitung luas seitiga dengan perintah fungsi dengan alas={alas} dan tinggi={tinggi} memiliki luas={hitung_luas_segitiga(10, 3)}")
print(f"\ntotal luas seitiga dengan perintah fungsi {hitung_luas_segitiga(50, 5)}")
print(f"\ntotal luas seitiga dengan perintah fungsi {hitung_luas_segitiga(75, 10)}")


