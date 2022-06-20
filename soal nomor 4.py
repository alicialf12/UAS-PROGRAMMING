numberTree = [1,2,3, [4,5], [6, [7,8,9]]]

def tampilkanValue (pohon):
    if isinstance(pohon, list):
        for angka in pohon:
            tampilkanValue(angka)
    else:
        print(f'angka {pohon}')

tampilkanValue(numberTree)