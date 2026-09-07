# başlangıç_değeri
# while (şart):
#     değişim_miktarı


i = 0
while (i <= 7):
    if(i == 4):
        break #* döngüyü bırakır direk çıkar
    i += 1
    print(i)
print()

i = 0 
while (i <= 7):
    i += 1
    if(i == 4):
        continue #* döngünün başına döner, kendinden sonraki kodlar çalışmaz
    print(i)


# while (True):
#     name = input("isminizi giriniz: ")
#     if(name == ""):
#         continue
#     else:
#         break
# print(f"your name is {name}")