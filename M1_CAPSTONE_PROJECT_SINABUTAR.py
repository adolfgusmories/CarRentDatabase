# CAPSTONE PROJECT : RENTAL MOBIL               # BY MORIS
import os
os.system('cls') 
import time

# # Kode mobil
# # Merk Mobil
# # Tahun mobil
# # Warna mobil
# # Harga sewa

# # DATA AWAL 
mobil_1 = {
    'kode' : '10T',
    'merk' : 'Toyota',
    'tahun': 2020,
    'warna': 'Hitam',
    'harga': 500000
}
mobil_2 = {
    'kode' : '10H',
    'merk' : 'Honda',
    'tahun': 2019,
    'warna': 'Putih',
    'harga': 600000
}
mobil_3 = {
    'kode' : '11H',
    'merk' : 'Hyundai',
    'tahun': 2022,
    'warna': 'Abu',
    'harga': 550000
}
template_mobil = {
    'kode' : '00X',
    'merk' : 'Xxxxx',
    'tahun': 0000,
    'warna': 'Xxxxx',
    'harga': 000000
}

daftar_mobil = [
    mobil_1,
    mobil_2,
    mobil_3,
]

# # Database username

# MENU AWAL
def tampilkan(tampilkan):
    if tampilkan == 'tampilan menu utama':
        return print('''
======= WELCOME TO SEMESTA'S CAR RENT DATABASE SYSTEM =======

Main Menu:
1. Show Car Data
2. Add Car Data
3. Edit Car Data
4. Delete Car Data
5. Account Setting
6. EXIT
''')
    elif tampilkan == 'tampilan menu 1':
        return print('''
======= MENU 1: CAR DATA ========

1. Show All Car Data
2. Show Certain Car Data
3. Back to Main Menu
''')
    elif tampilkan == 'tampilan menu 2':
        return print('''
======= MENU 2: ADD CAR DATA ========

1. Adding New Car Data
2. Back to Main Menu  
''')
    elif tampilkan == 'tampilan menu 3':
        return print('''
======= MENU 3: EDIT CAR DATA ========

1. Edit Certain Car Data
2. Back to Main Menu    
''')
    elif tampilkan == 'tampilan menu 4':
        return print('''
======= MENU 4: DELETE CAR DATA ========

1. Delete Certain Car Data
2. Back to Main Menu  
''')
    elif tampilkan == 'tampilan menu 5':
        return print('''
======= MENU 5: ACCOUNT SETTING ========

1. Change Password
2. Add New Account
3. Back to Main Menu    
''')
# daftar_akun = None
list_user = []
list_pass = []

# db = open('database.txt', 'r')
def list_akun():

    db = open('database.txt', 'r')
    for line in db:
        
        user_, pass_ = line.split(", ")
        pass_ = pass_.strip()
        list_user.append(user_)
        list_pass.append(pass_)


    return dict(zip(list_user, list_pass))

daftar_akun = list_akun()


# LOGIN SYSTEM
while True:

    print (f'''
    LOGIN
-------------------------''')
    # Input username
    username = input('Username: ') 
    
    # Jika username tidak ada di daftar_akun
    if username not in daftar_akun.keys():
        print("Account doesn't exist!")
        time.sleep(0.5)
        os.system('cls') 
        continue
    
    # Jika username ada dalam daftar_akun
    elif username in daftar_akun.keys():

        # Looping 3 kali kesempatan input password yg benar
        for salah_ in range(3,0,-1):

            password = input('Password: ')

            if password != daftar_akun[username]:
                if salah_ > 1:
                    print(f'Wrong password, {salah_ -1}x left \r\033[A                             \033[A' )
                    continue
                
                else:
                    print('Wrong password!')
                    print('---------- Please Re-login ----------')
                    quit()    

            # Jika password sudah benar
            elif password == daftar_akun[username]:
                print('---------- Login Success ----------                   \r')
                break
    break

# MAIN MENU
while True:            
# Memanggil function tampilan menu utama
    tampilkan('tampilan menu utama')

    # Pilih menu yg akan diakses
    menu = input('Choose number want to access [1-5]: ')
                    

# MENU 1
    while menu == '1':

        # Memanggil function tampilan menu 1
        tampilkan('tampilan menu 1')
        
        menu_1 = input('Choose number want to access [1-3]: ')

# MENU_1_1
        # MENAMPILKAN MENU_1 -> NOMOR 1 (KESELURUHAN DATA)
        if menu_1 == '1' and len(daftar_mobil) > 0:

            # Print header data mobil        
            print(f"{'Kode Mobil':^11} | {'Merk':^8} | {'Tahun':^6} | {'Warna':^6} | {'Harga Sewa':^6} ")
            print('-'*55)

            # Looping setiap data mobil dalam daftar_mobil
            for menu_1_ in range(len(daftar_mobil)):

                KODE = daftar_mobil[menu_1_]['kode']
                MERK = daftar_mobil[menu_1_]['merk']
                TAHUN = daftar_mobil[menu_1_]['tahun']
                WARNA = daftar_mobil[menu_1_]['warna']
                HARGA = daftar_mobil[menu_1_]['harga']
                
                # Print daftar_mobil
                print(f"{KODE:^11} | {MERK:^8} | {TAHUN:^6} | {WARNA:^6} | {HARGA:^6} ")
            print('*'*55)                          


        # JIKA DI daftar_mobil TIDAK ADA DATA
        elif menu_1 == '1' and len(daftar_mobil) == 0:
            
            print('----- NO DATA -----')
            print('*'*55)                          
            
# MENU_1_2
        # MENAMPILKAN MENU_1 NOMOR 2 (DATA YG DIPILIH)        
        elif menu_1 == '2' and len(daftar_mobil) > 0:

            # Input code mobil yg ingin ditampilkan
            kode_mobil = (input("Input car's code want to shows : ")).upper()

            # Looping code mobil (input) pada data mobil untuk mendapatkan indeksnya
            idx = next((index for (index, value) in enumerate(daftar_mobil) if value['kode'] == kode_mobil), None)

            # Jika code mobil termasuk dalam daftar_mobil
            if idx != None:

                print(f"{'Kode Mobil':^11} | {'Merk':^8} | {'Tahun':^6} | {'Warna':^6} | {'Harga Sewa':^6} ")
                print('-'*55)
    

                KODE = daftar_mobil[idx]['kode']
                MERK = daftar_mobil[idx]['merk']
                TAHUN = daftar_mobil[idx]['tahun']
                WARNA = daftar_mobil[idx]['warna']
                HARGA = daftar_mobil[idx]['harga']
                
                print(f"{KODE:^11} | {MERK:^8} | {TAHUN:^6} | {WARNA:^6} | {HARGA:^6} ")
                print('*'*55) 

            # Jika kode mobil tidak ada dalam daftar_mobil
            if idx == None:
                print('----- NO DATA -----')


        # JIKA DI daftar_mobil TIDAK ADA DATA
        elif menu_1 == '2' and len(daftar_mobil) == 0:
            
            print('----- NO DATA -----')
            print('*'*55)    

# MENU_1_3
        # KEMBALI KE MENU UTAMA
        elif menu_1 == '3':
            break

# MENU_1_input tidak ada di menu
        else:
            print('----- You input wrong number -----')


# MENU_2
    while menu == '2':

        # MEMANGGIL FUNCTION TAMPILKAN (TAMPILAN MENU 2)
        tampilkan('tampilan menu 2')
        
        menu_2 = input('Choose number want to access [1-2]:')

        # Memilih option 1 di sub menu
        if menu_2 == '1':
            kode_mobil = (input("Input car's code: ")).upper()

            idx = next((index for (index, value) in enumerate(daftar_mobil) if value['kode'] == kode_mobil), None)

            if idx != None:
                print('----- Data Already Exist -----')
               
            elif idx == None:

                # Membuat dictionary mobil_baru berdasarkan template_mobil
                mobil_baru = dict.fromkeys(template_mobil.keys())

                # Input data mobil baru
                mobil_baru['kode'] = kode_mobil
                mobil_baru['merk'] = input('Masukkan merk mobil: ').capitalize()
                mobil_baru['tahun'] = input('Masukkan tahun pembuatan mobil: ').capitalize()
                mobil_baru['warna'] = input('Masukkan warna mobil: ').capitalize()
                mobil_baru['harga'] = input('Masukkan harga sewa mobil: ').capitalize()


                while True:
                        
                    konfirmasi = input('Do you want to save new data? (Y/N) :').upper()
                    print()

                    if konfirmasi == 'Y':
                        
                        daftar_mobil.append(mobil_baru)
                        print('----- Data Saved -----')
                        break

                    elif konfirmasi == 'N':
                        print('----- Data Not Saved -----')
                        break

                    else:
                        print('Please input right choice (Y/N)')
                        print()


        elif menu_2 == '2':
            break

        else:
            print('----- You input wrong number -----')

# MENU_3 : UBAH  DATA MOBIL
    while menu == '3':

        # MEMANGGIL FUNCTION TAMPILKAN (TAMPILAN MENU 3)
        tampilkan('tampilan menu 3')

        menu_3 = input('Choose number want to access [1-2]: ')

        # MENAMPILKAN MENU_3 NOMOR 1 (UBAH DATA MOBIL)
        if menu_3 == '1':
            
            kode_mobil = (input("Input car's code want to edit: ")).upper()

            # LOOPING APAKAH ADA kode_mobil DI daftar_mobil
            idx = next((index for (index, value) in enumerate(daftar_mobil) if value['kode'] == kode_mobil), None)

            if idx == None:
                print("----- Data doesn't exist! -----")

            elif idx != None:

                print(f"{'Kode Mobil':^11} | {'Merk':^8} | {'Tahun':^6} | {'Warna':^6} | {'Harga Sewa':^6} ")
                print('-'*55)

                # VALUE TIAP KEY PADA daftar_mobil INDEX KE-idx
                KODE = daftar_mobil[idx]['kode']
                MERK = daftar_mobil[idx]['merk']
                TAHUN = daftar_mobil[idx]['tahun']
                WARNA = daftar_mobil[idx]['warna']
                HARGA = daftar_mobil[idx]['harga']
                
                # PRINT daftar_mobil index ke-idx
                print(f"{KODE:^11} | {MERK:^8} | {TAHUN:^6} | {WARNA:^6} | {HARGA:^6} ")
                print('*'*55) 

                # LOOPING KONFIRMASI AWAL
                while True:
                        
                    konfirmasi = input('Do you want to continue edit data? (Y/N) :').upper()
                    print()

                    if konfirmasi == 'Y':
                        
                        # KETERANGAN YANG INGIN DIUBAH
                        edit_ = (input('Which description want to edit: ')).lower()

                        # Cek apakah keterangan edit_ ada di keys template_mobil
                        if edit_ in template_mobil.keys():
                                                    
                            # INPUT VALUE KETERANGAN YANG BARU
                            ket_baru = (input(f'Input new {edit_.capitalize()} data: ')).title()
                            
                            konfirmasi_2 = input('Do you want to save the changes (Y/N) ?').upper()

                            if konfirmasi_2 == 'Y':

                                # UPDATE DATA BARU daftar_mobil index ke-idx dengan key edit_
                                daftar_mobil[idx][edit_] = ket_baru
                                print('----- Data Saved -----')
                                break

                            elif konfirmasi_2 == 'N':
                                print('----- Data Not Saved -----')
                                break

                            # Jika jawaban konfirmasi ke-2 bukan Y/N
                            else:
                                print('Please input right choice (Y/N)')
                                print()   
                        
                        # Jika edit_ tidak ada di key template_mobil
                        else:
                            print("----- Description Doesn't Exist -----")

                    # Jika tidak melanjutkan ubah data, kembali ke Menu 3
                    elif konfirmasi == 'N':
                        print('Back to Menu 3')
                        break
                    
                    # Jika jawaban konfirmasi bukan Y/N
                    else:
                        print('Please input right choice (Y/N)')
                        print()

        # Kembali ke Menu Utama
        elif menu_3 == '2':
            break

        else:
            print('You input wrong number')

# MENU_4 : HAPUS DATA MOBIL
    while menu == '4':

        # Memamnggil function tampilkan(tampilan menu 4)
        tampilkan('tampilan menu 4')
        
        menu_4 = input('Choose number want to access [1-2]:')

        if menu_4 == '1':

            # Input kode mobil yg ingin dihapus
            kode_mobil = (input("Input car's code want to delete: ")).upper()

            # Looping kode_mobil di daftar_mobil
            idx = next((index for (index, value) in enumerate(daftar_mobil) if value['kode'] == kode_mobil), None)

            if idx == None:
                print("----- Data Doesn't Exist -----")

            elif idx != None:

                # Menampilkan data code mobil yg dimaksud
                print(f"{'Kode Mobil':^11} | {'Merk':^8} | {'Tahun':^6} | {'Warna':^6} | {'Harga Sewa':^6} ")
                print('-'*55)
    
                KODE = daftar_mobil[idx]['kode']
                MERK = daftar_mobil[idx]['merk']
                TAHUN = daftar_mobil[idx]['tahun']
                WARNA = daftar_mobil[idx]['warna']
                HARGA = daftar_mobil[idx]['harga']
                
                print(f"{KODE:^11} | {MERK:^8} | {TAHUN:^6} | {WARNA:^6} | {HARGA:^6} ")
                print('*'*55)

                # Looping konfirmasi data apakah akan dilanjutkan untuk dihapus
                while True:

                    konfirmasi = input('Do you sure want to delete this data? (Y/N) :').upper()

                    if konfirmasi == 'Y':
                        if username == list_user[0]:
                            for salah_ in range(3,0,-1):
                                print(' ')
                                print('Please input your password')
                                pass_hapus = input('Password: ')
                                if pass_hapus != daftar_akun['admin']:
                                    if salah_ > 1:
                                        print('\r\033[A                             \033[A')
                                        print(f'Wrong password, {salah_ - 1}x left' )
                                        continue
                                    else:
                                        print()
                                        print('----- Access Denied -----')
                                        print('Back to Sub Menu 4')
                                       

                                else:
                                    break
    

                            if pass_hapus == daftar_akun['admin']:
                                
                                del daftar_mobil[idx]
                                
                                print('----- Data Deleted -----')

                                break
                            break

                        else:                        
                            print('Only admin can access this option, please login by administator account')
                            print (f'''
    LOGIN
-------------------------''')
                            user_input = input('Username: ') 
                                                        
                            if user_input != list_user[0]:
                                print('Please login by administrator account')
                                continue

                            elif user_input == list_user[0]:
                            
                                for salah_ in range(3,0,-1):

                                    pass_hapus = input('Password: ')

                                    if pass_hapus != daftar_akun['admin']:
                                        if salah_ > 1:
                                            print(f'Wrong password! ({salah_ -1}x left) \r\033[A                             \033[A' )
                                            continue
                                        
                                        else:
                                            print('Access Denied!                    \r')
                                            print('---------- Back to Sub Menu 4 ----------')
                                            break    
                                
                                    elif pass_hapus == daftar_akun['admin']:
                                        
                                        del daftar_mobil[idx]

                                        print('----- Data Deleted -----                   \r')
                                        break
                        break


                    elif konfirmasi == 'N':

                        break

                    elif konfirmasi not in ['Y','N']:
                        print('Please input right choice (Y/N)')
                        print()
                    else:
                        break    


        elif menu_4 == '2':
            break
        else:
            print('You input wrong number')

# MENU_5 : ACCOUNT SETTING
    while menu == '5':
        tampilkan('tampilan menu 5')

        menu_5 = input('Choose number want to access [1-3]: ')

        if menu_5 == '1':   # Change Password
            
            print('You need to input your current password first')


            for salah_ in range(3,0,-1):
                pass_ganti = input('Password: ')
                if pass_ganti != daftar_akun[username]:

                    if salah_ > 1:
                        print(f'Wrong password! ({salah_ -1}x left) \r\033[A                             \033[A' )
                        continue
                
                    else:
                        print('Wrong password! Back to Sub Menu 5')
                
                elif pass_ganti == daftar_akun[username]:
                    
                    print('\n')
                    print('Please input your new password')
                    pass_new = input('New Password         : ')

                    while True:
                        pass_new2 = input('Confirm New Password : ')

                        if pass_new != pass_new2:
                            print("Password didn't match \r\033[A                                                              \033[A")
                            continue

                        elif pass_new == pass_new2:
                            daftar_akun[username] = pass_new
                            print('----- Password Successfully Changed -----')
                            

                        break
                    break
        elif menu_5 == '2':
            
            if username != list_user[0]:
                print('''
Only admin can access this option, please login by administator account''')
                print (f'''
    LOGIN
-------------------------''')
                while True:
                    user_input = input('Username: ') 
                                                        
                    if user_input != list_user[0]:
                        print('Please login by administrator account \r\033[A                             \033[A')
                        continue

                    elif user_input == list_user[0]:
                        print('\n\033[A                                               \033[A')
                    
                        for salah_ in range(3,0,-1):

                            pass_hapus = input('Password: ')

                            if pass_hapus != daftar_akun['admin']:
                                if salah_ > 1:
                                    print(f'Wrong password! ({salah_ -1}x left) \r\033[A                             \033[A' )
                                    continue
                                
                                else:
                                    print('Access Denied!                    \r')
                                    print('---------- Back to Sub Menu 5 ----------')
                                    continue   

                            elif pass_hapus == daftar_akun['admin']:
                                print('----- Login Success -----                   ')
                                            
                                akun_input = input('Input new username: ')

                                if akun_input in list_user:
                                    print('----- Account Exist -----')
                                    break

                                elif akun_input not in list_user:

                                    pass_new = input('Input new password: ')
                                    while True:
                                        pass_new2 = input('Confirm new password: ')

                                        if pass_new != pass_new2:
                                            print("Password didn't match \r\033[A                                                              \033[A")
                                            continue

                                        elif pass_new == pass_new2:
                                            db = open('database.txt', 'a')
                                            db.write(akun_input+', '+pass_new+ '\n')

                                            daftar_akun = list_akun()
                                            print(daftar_akun)
                                            
                                            print('----- Account Successfully Registered -----')

                                            break

                                break
                        break

            elif username == list_user[0]:
                print()
                akun_input = input('Input new username: ')

                if akun_input in list_user:
                    print('----- Account Exist -----')
                    continue

                elif akun_input not in list_user:

                    pass_new = input('Input new password: ')
                    while True:
                        pass_new2 = input('Confirm new password: ')

                        if pass_new != pass_new2:
                            print("Password didn't match \r\033[A                                                              \033[A")
                            continue

                        elif pass_new == pass_new2:
                            db = open('database.txt', 'a')
                            db.write(akun_input+', '+pass_new+ '\n')
                            
                            
                            daftar_akun = list_akun()
                            
                            print('----- Account Succesfully Registered -----')
                            break

                    break

            
        elif menu_5 == '3':
            print('----- Back to Main Menu -----')
            break

        else:
            print('You input wrong number')



    if menu not in ['1','2','3','4','5','6']:
        print('----- You input wrong number -----')
        
        
# MENU_6
    elif menu == '6':
        print("===== THANK YOU FOR ACCESSING SEMESTA'S DATABASE SYSTEM =====")
        print("===============            SEE YA!            ===============")
        break

    