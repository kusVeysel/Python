
#? \" ve \'
#* çift tırnak içinde çift tırnak ,tek tırnak içinde tek tırnak olmaz , ancak \ karakteriyle yapılabilir
print("Hello\" World!")
print('Hello\' World!')

#? \\
#* Backslash atmak içinde yine \ karakteri kullanılır
print("Hello\\ World!")

#? \n
#* Alt satıra geçmek için \n kullanılır
print("Hello \nWorld!")

#? \r
#* carriage return imleci satırın başına taşır; görünen sonuç terminale göre değişebilir
print("Hello World! \rPython")

#? \t
#* Bir tap boşluk için \t kullanılır
print("Hello\tWorld!")

#? \b
#* \b backspace karakteridir; imleci bir karakter geri taşıyabilir, boşluk eklemez
print("Hello\bWorld!")

#?
#* Oktal sayıları harfe yazar
print("\120\171\164\150\157\156")

#?
#* HekzaDekimal sayıları harfe çevirip yazar
print("\x50\x79\x74\x68\x6F\x6E")