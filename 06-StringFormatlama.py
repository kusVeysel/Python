 #? STRING FORMATLAMA({:})

isim = "Veysel KUŞ"
yas = 34
fiyat = 19.563480

#? f-string
#* Stringin başına f yazarak süslü parantez içine değişken yazılır.
print("------------------------------------------")
print("f'Merhaba {isim}, yaşım {yas}' →", f"Merhaba {isim}, yaşım {yas}")
print("------------------------------------------")

#? format()
#* String içine sıralı veya isimli değişken yerleştirir.
print("'Merhaba {}, yaşım {}'.format(isim, yas) →", "Merhaba {}, yaşım {}".format(isim, yas))
print("------------------------------------------")
print("'Merhaba {0}, yaşım {1}'.format(isim, yas) →", "Merhaba {0}, yaşım {1}".format(isim, yas))
print("------------------------------------------")

#? Ondalık basamak
#* :.2f, virgülden sonra 2 basamak gösterir.
print("f'{19.563480:.2f}' →", f"{19.563480:.2f}")
print("------------------------------------------")

#? Hizalama
#* <: Sola, >: Sağa, ^: Ortaya hizalar. Sayı toplam genişliği belirtir.
print("'Ad: {:<15}'.format('Veysel') →", "Ad: {:<15},sola".format('Veysel'))
print("------------------------------------------")
print("'Ad: {:>15}'.format('Veysel') →", "Ad: {:>15},sağa".format('Veysel'))
print("------------------------------------------")
print("'Ad: {:^15}'.format('Veysel') →", "Ad: {:^15},ortaya".format('Veysel'))
print("------------------------------------------")

#? İşaret
#* + → Pozitif ve negatif sayıların işaretini gösterir.
#* - → Negatif sayıların işaretini gösterir (varsayılan).
#* boşluk → Pozitif sayının önüne boşluk, negatif sayının önüne - koyar.
print("'{:+}'.format(7) →", "{:+}".format(7))
print("------------------------------------------")
print("'{:+}'.format(7) →", "{:+}".format(-7))
print("------------------------------------------")
print("'{:-}'.format(7) →", "{:-}".format(7))
print("------------------------------------------")
print("'{:-}'.format(-7) →", "{:-}".format(-7))
print("------------------------------------------")
print("'{: }'.format(7) →", "{: }".format(7))
print("------------------------------------------")
print("'{: }'.format(-7) →", "{: }".format(-7))
print("------------------------------------------")

#? Binlik ayırıcı
#* , veya _ sayıları binlik gruplara ayırır.
print("'{:,}'.format(543854055867) →", "{:,}".format(543854055867))
print("------------------------------------------")
print("'{:_}'.format(543854055867) →", "{:_}".format(543854055867))
print("------------------------------------------")

#? Sayı tabanları
#* b: İkilik, o: Sekizlik, x: Onaltılık tabanda gösterir.
print("'{:b}'.format(6) →", "{:b}".format(6))
print("------------------------------------------")
print("'{:o}'.format(19) →", "{:o}".format(19))
print("------------------------------------------")
print("'{:x}'.format(250) →", "{:x}".format(250))
print("------------------------------------------")

#? Bilimsel gösterim
#* e, sayıyı bilimsel gösterim biçiminde yazar.
print("'{:e}'.format(5) →", "{:e}".format(5))
print("------------------------------------------")

#? Unicode karakter
#* c, tam sayı karşılığındaki Unicode karakterini gösterir.
print("'{:c}'.format(199) →", "{:c}".format(199))
print("------------------------------------------")

#? Yüzde
#* %, ondalık sayıyı yüzde biçiminde gösterir.
print("'{:.1%}'.format(0.756) →", "{:.1%}".format(0.756))
