import random #pass admin = admin123
import time
from prettytable import PrettyTable
Sign_up = 0
#coin
coin = 1000
#inventory
king = 0
mumen = 0
mask = 0
genos = 0
saitama = 0
#change rate standar
rate_c = 10000
rate_b = 2000
rate_a = 500
rate_s = 100
rate_ssr = 1
#table harga
table_harga = PrettyTable()
table_harga.field_names = ["No","Figure", "Grade", "Harga"]
table_harga.add_row(["1","king", "C", "100"])
table_harga.add_row(["2","Mumen", "B", "500"])
table_harga.add_row(["3","mask", "A", "2000"])
table_harga.add_row(["4","Genos", "S", "10000"])
table_harga.add_row(["5","Saitama", "SSR", "100000"])
#table inv
def table_inv():
    tableinv = PrettyTable()
    tableinv.field_names = ["No","Figure", "Grade", "jumlah"]
    tableinv.add_row(["1","king", "C", f"{king}"])
    tableinv.add_row(["2","Mumen", "B", f"{mumen}"])
    tableinv.add_row(["3","mask", "A", f"{mask}"])
    tableinv.add_row(["4","Genos", "S", f"{genos}"])
    tableinv.add_row(["5","Saitama", "SSR", f"{saitama}"])
    return tableinv
#table rate
def table_rate():
    table_rate = PrettyTable()
    table_rate.field_names = ["No","Figure", "Grade", "rate"]
    table_rate.add_row(["1","king", "C", f"{rate_c}"])
    table_rate.add_row(["2","Mumen", "B", f"{rate_b}"])
    table_rate.add_row(["3","mask", "A", f"{rate_a}"])
    table_rate.add_row(["4","Genos", "S", f"{rate_s}"])
    table_rate.add_row(["5","Saitama", "SSR", f"{rate_ssr}"])
    return table_rate
def piltidakvalid():
    print("\npilihan tidak valid ! ")
def pertidakvalid():
    print("\nperintah tidak valid ! ")
def angtidakvalid():
    print("\nangka tidak valid ! ")
def jwbtidakvalid():
    print("\njawaban tidak valid")
def garis():
    print("---------------------------------------------------------------")
while True:
    try:
        pil1 = int(input("""-----------------Selamat Datang Di Gacha F3000-----------------
1.SIGN UP
2.LOG IN
3.ADMIN
4.EXIT
Pilihan: """))
        if pil1 == 1:
            print("\n----------------------------Sign Up----------------------------")
            user_id = input("User ID: ")
            password = input("Password: ")
            print("---------------------------------------------------------------")
            Sign_up += 1

        elif pil1 == 2:
                if Sign_up == 0:
                    garis()
                    print("\nKamu Belum Memiliki Akun! ")
                elif Sign_up >= 1:
                    print("\n-----------------------------Login-----------------------------")
                    user_id1 = input("User ID: ")
                    password1 = input("Password: ")
                    print("---------------------------------------------------------------")
                    if user_id == user_id1 and password == password1:
                        print("-----------------------------Lobby-----------------------------")
                        print(F"\n{user_id}, Selamat Datang Di Gacha F3000")
                        time.sleep(1)
                        while True:
                            try:
                                pil2 = int(input("""\n-----------------------------Lobby-----------------------------
1.Cek Coins
2.Inventory
3.GACHA                                               
4.Adventure
5.Log Out
Pilihan: """))
                                if pil2 == 1:
                                    garis()
                                    print(f"\nKamu Memiliki Sebanyak {coin} coin")
                                elif pil2 == 2:
                                    print(f"""\n---------------------------INVENTORY---------------------------""")
                                    show = table_inv()
                                    print(show)
                                    print(f"kamu memiliki total {king + mumen + mask + genos + saitama} figure")
                                    try:
                                        pil3 = int(input("""\n1.jual
2.Jual Semua
3.Balik Lobby                                                                                                              
Pilihan: """))
                                        if pil3 == 1:
                                            while True:
                                                print("\n-----------------------------SELL------------------------------")
                                                print(table_harga)
                                                pil4 = int(input(f"""6.Balik Lobby
pilihan: """))
                                                if pil4 == 1:
                                                    if king > 0:
                                                        garis()
                                                        print("\nking seharga 100 coin")
                                                        jual1 = int(input("mau jual berapa: "))
                                                        if jual1 > king or jual1 <= 0:
                                                            print("jual tidak valid")
                                                        else:
                                                            king -= jual1*1 
                                                            coin += jual1*100
                                                    else:
                                                        garis()
                                                        print("kamu tidak memiliki king!") 
                                                elif pil4 == 2:
                                                    if mumen > 0:
                                                        garis()
                                                        print("\nmumen seharga 500 coin")
                                                        jual2 = int(input("mau jual berapa: "))
                                                        if jual2 > mumen or jual2 <= 0:
                                                            print("jual tidak valid")
                                                        else:
                                                            mumen -= jual2*1
                                                            coin += jual2*500 
                                                    else:
                                                        garis()
                                                        print("kamu tidak memiliki mumen!")
                                                elif pil4 == 3:
                                                    if mask > 0:
                                                        garis()
                                                        print("\nmask seharga 2000 coin")
                                                        jual3 = int(input("mau jual berapa: "))
                                                        if jual3 > mask or jual3 <= 0:
                                                            print("jual tidak valid")
                                                        else:
                                                            mask -= jual3*1
                                                            coin += jual3*2000 
                                                    else:
                                                        garis()
                                                        print("kamu tidak memiliki mask!")
                                                elif pil4 == 4:
                                                    if genos > 0:
                                                        garis()
                                                        print("\ngenos  seharga 10000 coin")
                                                        jual4 = int(input("mau jual berapa: "))
                                                        if jual4 > genos or jual4 <= 0:
                                                            print("jual tidak valid")
                                                        else:
                                                            genos -= jual4*1 
                                                            coin += jual4*10000 
                                                    else:
                                                        garis()
                                                        print("kamu tidak memiliki genos!")
                                                elif pil4 == 5:
                                                    if saitama > 0 :
                                                        garis()
                                                        print("\nsaitama seharga 100000 coin")
                                                        jual5 = int(input("mau jual berapa: "))
                                                        if jual5 > saitama or jual5 <= 0:
                                                            print("jual tidak valid")
                                                        else:
                                                            saitama -= jual5*1
                                                            coin += jual5*100000 
                                                    else:
                                                        garis()
                                                        print("kamu tidak memiliki saitama!")
                                                elif pil4 == 6:
                                                    break
                                                else:
                                                    jwbtidakvalid()
                                        elif pil3 == 2:
                                            while True:
                                                if king == 0 and mumen == 0 and mask == 0 and genos == 0 and saitama == 0:
                                                    garis()
                                                    print("kamu miskin gak punya apa apa")
                                                    break
                                                else:
                                                    garis()
                                                    coin += king*100 
                                                    king -= king
                                                    coin += mumen*500 
                                                    mumen -= mumen
                                                    coin += mask*2000 
                                                    mask -= mask
                                                    coin += genos*10000
                                                    genos -= genos
                                                    coin += saitama*100000 
                                                    saitama -= saitama
                                                    print(f"coin mu menjadi sebanyak {coin} coin")
                                                    break
                                        elif pil3 == 3:
                                            print("")
                                        else:
                                            print("\npilihan tidak valid")
                                    except ValueError:
                                        print("\npilihan tidak valid")
                                elif pil2 == 3:
                                    if coin < 100:
                                        garis()
                                        print("\ncoin anda tidak cukup untuk gacha")
                                        print(f"coinmu sebanyak {coin}")
                                    else:
                                        while True:
                                            try:
                                                pil8 = int(input("""--------------------------GACHA LOBBY--------------------------
1.Gacha 1X
2.Gacha Input                                          
3.Gacha ALL IN
4.Keluar
pilihan: """))
                                                if pil8 == 1:
                                                    if coin < 100:
                                                        garis()
                                                        print("coinmu tidak cukup")
                                                    else:
                                                        num =random.randint(1,10000)
                                                        if num <= rate_ssr:
                                                            garis()
                                                            print("???")
                                                            time.sleep(1)
                                                            print("Apa itu?")
                                                            time.sleep(2)
                                                            print("KAMU MENDAPATKAN SAITAMA GRADE SSR")
                                                            time.sleep(3)
                                                            coin -= 100
                                                            saitama += 1
                                                            print(f"coinmu sebanyak {coin}")                
                                                        elif num <= rate_s:
                                                            garis()
                                                            print("\nGrade S Genos ")
                                                            coin -= 100
                                                            genos += 1
                                                            print(f"coinmu sebanyak {coin}")
                                                        elif num <= rate_a:
                                                            garis()
                                                            print("\nGrade A mask ")
                                                            coin -= 100
                                                            mask += 1
                                                            print(f"coinmu sebanyak {coin}")
                                                        elif num <= rate_b:
                                                            garis()
                                                            print("\nGrade B mumen")
                                                            coin -= 100
                                                            mumen += 1
                                                            print(f"coinmu sebanyak {coin}")
                                                        elif num <= rate_c:
                                                            garis()
                                                            print("\nGrade C king")
                                                            coin -= 100
                                                            king += 1
                                                            print(f"coinmu sebanyak {coin}")
                                                elif pil8 == 2:
                                                    try:
                                                        print(f"kamu dapat gacha maksimal {coin/100}X")
                                                        banyak_gacha = int(input("berapa banyak, yang ingin kamu gacha: "))
                                                        if banyak_gacha > coin/100:
                                                            angtidakvalid()
                                                        elif banyak_gacha > 0:
                                                            garis()
                                                            for i in range(banyak_gacha):
                                                                i = banyak_gacha
                                                                num =random.randint(1,10000)
                                                                if i > 0:
                                                                    if num <= rate_ssr:
                                                                        print("???")
                                                                        time.sleep(1)
                                                                        print("Apa itu?")
                                                                        time.sleep(2)
                                                                        print("KAMU MENDAPATKAN SAITAMA GRADE SSR")
                                                                        time.sleep(3)
                                                                        coin -= 100
                                                                        saitama += 1   
                                                                        i -= 1         
                                                                    elif num <= rate_s:
                                                                        time.sleep(1)
                                                                        print("Grade S Genos ")
                                                                        coin -= 100
                                                                        genos += 1
                                                                        i -= 1
                                                                    elif num <= rate_a:
                                                                        time.sleep(1)
                                                                        print("Grade A mask ")
                                                                        coin -= 100
                                                                        mask += 1
                                                                        i -= 1
                                                                    elif num <= rate_b:
                                                                        time.sleep(1)
                                                                        print("Grade B mumen")
                                                                        coin -= 100
                                                                        mumen += 1
                                                                        i -= 1
                                                                    elif num <= rate_c:
                                                                        time.sleep(1)
                                                                        print("Grade C king")
                                                                        coin -= 100
                                                                        king += 1
                                                                        i -= 1
                                                                if i <= 0:
                                                                    break
                                                        else:
                                                            garis()
                                                            angtidakvalid()
                                                    except ValueError:
                                                        garis()
                                                        angtidakvalid()
                                                elif pil8 == 3:
                                                    if coin < 100:
                                                        garis()
                                                        print("coin mu tidak cukup")
                                                    else:
                                                        try:
                                                            garis()
                                                            print(f"kamu akan gacha sebanyak {coin/100}X")
                                                            pil9 = int(input(f"""\nALERT SELAMA PROCESS BERJALAN KAMU TIDAK BISA KELUAR ! 
YAKIN? 
1.ENGGA
2.IYA
PILIHAN: """))
                                                            garis()
                                                            if pil9 == 1:
                                                                break
                                                            elif pil9 == 2:
                                                                while True:
                                                                    if coin >= 100:
                                                                        num =random.randint(1,10000)
                                                                        if num <= rate_ssr:
                                                                            print("???")
                                                                            time.sleep(1)
                                                                            print("Apa itu?")
                                                                            time.sleep(2)
                                                                            print("KAMU MENDAPATKAN SAITAMA GRADE SSR")
                                                                            time.sleep(3)
                                                                            coin -= 100
                                                                            saitama += 1            
                                                                        elif num <= rate_s:
                                                                            time.sleep(1)
                                                                            print("Grade S Genos ")
                                                                            coin -= 100
                                                                            genos += 1
                                                                        elif num <= rate_a:
                                                                            time.sleep(1)
                                                                            print("Grade A mask ")
                                                                            coin -= 100
                                                                            mask += 1
                                                                        elif num <= rate_b:
                                                                            time.sleep(1)
                                                                            print("Grade B mumen")
                                                                            coin -= 100
                                                                            mumen += 1
                                                                        elif num <= rate_c:
                                                                            time.sleep(1)
                                                                            print("Grade C king")
                                                                            coin -= 100
                                                                            king += 1
                                                                    else:
                                                                        break
                                                            else:
                                                                piltidakvalid()
                                                        except ValueError:
                                                            angtidakvalid()
                                                elif pil8 == 4:
                                                    break
                                                else: 
                                                    piltidakvalid()
                                            except ValueError:
                                                angtidakvalid()
                                elif pil2 == 4:
                                    garis()
                                    print("COMING SOON, please support aku")
                                    print("dengan mengirim email di darmapala9945@gmail.com")
                                elif pil2 == 5:
                                    break
                                else:
                                    print("\npilihan tidak valid !")
                            except ValueError:
                                print("\npilihan tidak valid !")
                    else:
                        print("ID Atau Password Tidak Sesuai ! ")

        elif pil1 == 3:
            password_admin = input("Pass admin: ")
            if password_admin == "admin123":
                print("\n--------------------selamat datang admin 01--------------------")
                while True:
                    pil5 = int(input("""\n1.Nambah coin
2.Ubah rate gacha
3.Nambah Figure
4.keluar admin
Pilihan: """))
                    if pil5 == 1:
                        garis()
                        print(f"\ncoin = {coin}")
                        nambah = int(input("add coin: "))
                        coin += nambah
                    elif pil5 == 2:
                            try:
                                garis()
                                print("""untuk change rate default pada 1-10000 random:
saitama <= 1, genos <= 100, mask <= 500, mumen <= 2000, king <= 10000 
yang diubah rate pada angka tersebut""")
                                print("------------------------------RATE-----------------------------")
                                show1 = table_rate()
                                print(show1)
                                pil6 = int(input(f"""6.Balik ke Command
pilihan: """))
                                if pil6 == 1:
                                    try:
                                        garis()
                                        rate_c = int(input("Rate C: "))
                                        if rate_c <= 0 or rate_c > 10000:
                                            angtidakvalid()
                                    except ValueError:
                                        angtidakvalid()
                                elif pil6 == 2:
                                    try:
                                        garis()
                                        rate_b = int(input("Rate B: "))
                                        if rate_b <= 0 or rate_b > 10000:
                                            angtidakvalid()
                                    except ValueError:
                                        angtidakvalid()
                                elif pil6 == 3:
                                    try:
                                        garis()
                                        rate_a = int(input("Rate A: "))
                                        if rate_a <= 0 or rate_a > 10000:
                                            angtidakvalid()
                                    except ValueError:
                                        angtidakvalid()
                                elif pil6 == 4:
                                    try:
                                        garis()
                                        rate_s = int(input("Rate S: "))
                                        if rate_s <= 0 or rate_s > 10000:
                                            angtidakvalid()
                                    except ValueError:
                                        angtidakvalid()
                                elif pil6 == 5:
                                    try:
                                        garis()
                                        rate_ssr = int(input("Rate SSR: "))
                                        if rate_ssr <= 0 or rate_ssr > 10000:
                                            angtidakvalid()
                                    except ValueError:
                                        angtidakvalid()
                                elif pil6 == 2:
                                    break
                            except ValueError:
                                print("pilihan tidak valid !")
                    elif pil5 == 3:
                        while True:
                            print("\n-----------------pilih yang ingin ditambahkan------------------")
                            show = table_inv()
                            print(show)
                            pil7 = int(input(f"""6.Balik ke Command
pilihan: """))
                            if pil7 == 1:
                                try:
                                    garis()
                                    nambah1 = int(input("Berapa yang ingin ditambahkan: "))
                                    if nambah1 > 0:
                                        king += nambah1
                                    else:
                                        print("\nangka tidak valid ! ")
                                except ValueError:
                                    print("\nharus angka ! ")
                            if pil7 == 2:
                                try:
                                    garis()
                                    nambah2 = int(input("Berapa yang ingin ditambahkan: "))
                                    if nambah2 > 0:
                                        mumen += nambah2
                                    else:
                                        print("\nangka tidak valid ! ")
                                except ValueError:
                                    print("\nharus angka ! ")
                            if pil7 == 3:
                                try:
                                    garis()
                                    nambah3 = int(input("Berapa yang ingin ditambahkan: "))
                                    if nambah3 > 0:
                                        mask += nambah3
                                    else:
                                        print("\nangka tidak valid ! ")
                                except ValueError:
                                    print("\nharus angka ! ")
                            if pil7 == 4:
                                try:
                                    garis()
                                    nambah4 = int(input("Berapa yang ingin ditambahkan: "))
                                    if nambah4 > 0:
                                        genos += nambah4
                                    else:
                                        print("\nangka tidak valid ! ")
                                except ValueError:
                                    print("\nharus angka ! ")
                            if pil7 == 5:
                                try:
                                    garis()
                                    nambah5 = int(input("Berapa yang ingin ditambahkan: "))
                                    if nambah5 > 0:
                                        saitama += nambah5
                                    else:
                                        print("\nangka tidak valid ! ")
                                except ValueError:
                                    print("\nharus angka ! ")
                            elif pil7 == 6:
                                break
                            else:
                                piltidakvalid()
                    elif pil5 == 4:
                        break
                    else:
                        print("\npilihan tidak valid ! ")
            else:
                print("password salah ! ")
        elif pil1 == 4:
            print("\n----------------------Sampai Jumpa Kembali---------------------")
            break
        else:
            print("\npilihan tidak valid ! ")
    except ValueError:
        print("\npilihan tidak valid !")