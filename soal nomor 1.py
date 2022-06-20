dataMhs = [["82122328","Dwiky", "Ilmu hukum"], ["82122331", "Ratih", "Ilmu hukum"], ["82122330", "Kana", "Ilmu hukum"]]
h = 0
print("Silahkan pilih nama mahasiswa berikut: ")
for i in dataMhs:
    print(f"{h+1}. {dataMhs[h][1]}")
    h = h + 1

user = int(input("Pilihan anda: "))

if user == 1:
    print(dataMhs[0])
elif user == 2:
    print(dataMhs[1])
elif user == 3:
    print(dataMhs[2])