sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
  print(f"{sayi} çift sayıdır.")
else:
  print(f"{sayi} tek sayıdır.")
  notu = int(input("Notunuzu girin: "))

if 90 <= notu <= 100:
  harf_notu = "A"
elif 80 <= notu <= 89:
  harf_notu = "B"
elif 70 <= notu <= 79:
  harf_notu = "C"
elif 60 <= notu <= 69:
  harf_notu = "D"
elif 0 <= notu <= 59:
  harf_notu = "F"
else:
    harf_notu = "Geçersiz Not Girişi"

print(f"Harf notunuz: {harf_notu}")
yas = int(input("Yaşınızı girin: "))

if 0 <= yas <= 12:
  yas_grubu = "Çocuk"
elif 13 <= yas <= 19:
  yas_grubu = "Genç"
elif 20 <= yas <= 59:
  yas_grubu = "Yetişkin"
else:
  yas_grubu = "Yaşlı"

print(f"Yaş grubunuz: {yas_grubu}")