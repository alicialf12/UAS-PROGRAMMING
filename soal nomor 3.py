data = []
h = 0
while True:
    user = input("Masukkan angka: ")
    if user == 'n':
        break
    h += 1
    data.append(user)

jumlah = 0 
for nilai in data:
    jumlah += int(nilai)
jumlah = jumlah / h
print (jumlah)