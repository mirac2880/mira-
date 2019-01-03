def fakotriyel(numara):
    fak=1
    for i in range(1,numara+1):
        fak*=i
    print(fak)

sayi=int(input("bir sayı grirniz:"))
fakotriyel(sayi)

