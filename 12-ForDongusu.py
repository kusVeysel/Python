# for degisken in dizi:
# forEach gibi diziyi komple döner, her döngüde gelen değer degiskene atanır


fruits = ["Graphe","Orange","Strawberry","Pineapple","Melon","Matermelon"]

for fruit in fruits:
    print(fruit)
    if(fruit == "Orange"):
        continue
    if(fruit == "Strawberry"):
        break

for number in range(8): #* range(8): 0(dahil)'dan 8(dahil değil)'e sayı listesi oluşturur
    print(number, end = " ") #* end="": sonuna ne yazılacağı

for i in range(3):
    pass #* henüz doldurmadığımızda sonra doldurmak istediğimizde pass ya da ... kullanılır