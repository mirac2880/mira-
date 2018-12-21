dizi=[]
for i in range(5):
    a=input("bir sayı giriniz...")
    dizi.append(a)
dizi.sort(reverse=True)
print(dizi)

dosya=open(r"C:\221120181008\221120181008.txt","w")

for x in range(5):
    dosya.write(dizi[x]+" ")
