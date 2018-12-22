cümle=str(input("bir cümle giriniz"))
print("tersten:"+cümle[::-1])
cümlesplit=cümle.split()
print(cümlesplit)
for i in range(len (cümlesplit)):
    print(len(cümlesplit[i]))

for i in range(len(cümlesplit)):
    kelime=cümlesplit[i]
    kelime1=kelime[::-1]
    print(kelime1)
