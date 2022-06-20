import mysql.connector
import os
from prettytable import PrettyTable

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mahasiswa"
)


def tambah():
    cursor = db.cursor()
    os.system('cls')
    name = input('Masukkan Nama: ')
    nim = input('Masukkan Nim (6 digit tanpa titik): ')
    if len(nim) != 8:
        print('nim salah')
        tambah()
        quit()
    prodi = input('Masukkan Program Studi: ')
    gender = input('Pilih Jenis Kelamin (m/f): ')
    if gender == 'm':
        gender = 'male'
    elif gender == 'f':
        gender = 'female'
    else:
        print('pilihan salah')
        tambah()
        quit()
    address = input('Masukkan alamat: ')
    sql = "insert into data(name,nim,prodi,gender,address) values(%s,%s,%s,%s,%s)"
    val = (name, nim, prodi, gender, address)
    cursor.execute(sql, val)
    db.commit()
    print("Data berhasil ditambahkan")


def ubah():
    cursor = db.cursor()
    update = input('Pilih data mahasiswa yang akan diubah (berdasarkan id): ')
    os.system('cls')
    name = input('Masukkan Nama baru: ')
    nim = input('Masukkan Nim baru (6 digit tanpa titik): ')
    if len(nim) != 8:
        print('nim salah')
        tambah()
        quit()
    prodi = input('Masukkan Program Studi baru: ')
    gender = input('Pilih Jenis Kelamin (m/f): ')
    if gender == 'm':
        gender = 'male'
    elif gender == 'f':
        gender = 'female'
    else:
        print('pilihan salah')
        tambah()
        quit()
    address = input('Masukkan alamat baru: ')
    sql = "UPDATE data SET name=%s,nim=%s,prodi=%s,gender=%s,address=%s WHERE id=%s"
    val = (name, nim, prodi, gender, address, update)
    cursor.execute(sql, val)
    db.commit()
    print("Data berhasil diubah")


def hapus():
    cursor = db.cursor()
    delete = input('Masukkan ID Mahasiswa yang akan dihapus: ')
    sql = "DELETE FROM data WHERE id=%s" % delete
    cursor.execute(sql)
    db.commit()
    print('Data berhasil dihapus')


def menu():
    cursor = db.cursor()
    sql = "SELECT * FROM data"
    cursor.execute(sql)
    hasil = cursor.fetchall()
    t = PrettyTable(['id', 'name', 'nim', 'prodi', 'gender', 'address'])
    os.system('cls')
    for row in hasil:
        t.add_row(row)
    print(t)

    print('DAFTAR PERINTAH')
    print('1.Tambah Data')
    print('2.Ubah Data')
    print('3.Hapus Data')
    print('Ketik exit jika ingin keluar')
    menu = input('Pilih Menu(1/2/3/exit): ')

    if menu == '1':
        tambah()
    if menu == '2':
        ubah()
    if menu == '3':
        hapus()
    elif menu == 'exit':
        os.system('cls')
        quit()


if __name__ == "__main__":
    while(True):
        menu()