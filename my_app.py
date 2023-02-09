not_girildi = 1
records = []

while True:
    print("1-Notlari Oku")
    print("2-Not Gir")
    print("3-Notlari Kayit Et")
    print("4-Cikis")

    choice = int(input("Lutfen yapmak istediginiz islemi giriniz:"))

    if choice == 1:
        if not_girildi == 1:
            print("Not Girmeniz Gerekmektedir..")
        else:
            for i, record in enumerate(records):
                print(f"{i + 1}. {record}")
    elif choice == 2:
        not_girildi = 0
        record = input("Eklemek istediginiz kaydi girin")
        records.append(record)
    elif choice == 3:
        if not_girildi ==1:
            print("Not Girmeniz Gerekmektedir..")
        else:
            for i, record in enumerate(records):
                print(f"{i + 1}. {record}")
            record_index = int(input("Düzenlemek istediğiniz kaydin numarasini girin: ")) - 1
            if record_index < 0 or record_index >= len(records):
                print("Geçersiz kayit numarasi.")
            else:
                new_record = input("Yeni kaydi girin: ")
                records[record_index] = new_record
                print("Kayit başariyla güncellendi.")


    elif choice == 4:
        print("Cikis yapiliyor")
        break
    else:
        print("Hatali Tuslamaya Yaptiniz Tekrar Deneyiniz")
