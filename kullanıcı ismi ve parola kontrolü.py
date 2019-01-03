defkullanici="miracaltn44"
defparola="12345.m"

kullanici=input("kullanıcı adınızı giriniz:")
parola=input("şifrenizi giriniz:")
if((defkullanici==kullanici) and (defparola==parola)):
    print("sisteme hoşgeldiniz....")

elif((defkullanici!=kullanici) and (defparola==parola)):
    print("kullanıcı adınız hatalı!!")

elif((defkullanici==kullanici) and (defparola!=parola)):
    print("parolanız yanlış...")

else:
    print("kullanıcı ve parolanızı tekrar giriniz!!")

