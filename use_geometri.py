# from geometri.segitiga import hitung_luas_segitiga
import geometri.segitiga as gs

print(f"hitung_luas_segitiga {gs.hitung_luas_segitiga(10, 5)}")

from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegipanjang
from geometri.segitiga import hitung_luas_segitiga, info

print(info())
print(f"hitung_luas_segitiga {hitung_luas_segitiga(10, 5)}")

print(info_persegipanjang())
print(f"hitung_luas_persegi_panjang {hitung_luas_persegi_panjang(10, 5)}")
