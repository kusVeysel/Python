from app_class import PhoneBook

pb = PhoneBook()


while True:
    print("\nTelefon Rehberi")
    print("1-Kişi Ekle")
    print("2-Kişileri Listele")
    print("3-Kişi Sil")
    print("4-Çıkış")

    choice = int(input("Seçim Yapınız: "))

    if(choice == 1):
        first_name = input("İsim: ")
        last_name = input("Soy İsim: ")
        phone = input("Telefon Numarası: ")
        pb.add_contact(first_name, last_name, phone)
    elif(choice == 2):
        pb.list_contacts()
    elif(choice == 3):
        name = input("Silmek için isim giriniz: ")
        pb.delete_contact(name)
    elif(choice == 4):
        print("Çıkış yapılıyor...")
        break
    else:
        print("Hatalı seçim, lütfen uygun seçim yapınız")
