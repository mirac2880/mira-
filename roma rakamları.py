from tkinter import *
from tkinter import messagebox

roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def sayigir():
    def dec2roman(number):
        if 1 <= number <= 3999:
            romanvalue = ("")
            if type(number) == float:
                integer, fractor = str(number).split('.')
                integer = int(integer)
                while len(fractor) > 3:
                    fra = list(fractor)
                    fra.pop()
                    fractor = ("".join(fra))
                fractor = int(fractor)
                return dec2roman(integer) + ('.') + dec2roman(fractor)
            for i, d in enumerate(decimal):
                while (number >= d):
                    number -= d
                    romanvalue += roman[i]
            return (romanvalue)
        else:

            messagebox.showinfo("Mesaj Baslik", "1-3888 Arasında Bir Sayı Giriniz.")

    il = giris.get()
    messagebox.showinfo("Mesaj Baslik", dec2roman(int(il)))


window = Tk()
window.geometry("250x250")
sayi = Label(window)
sayi.config( text="Bir Sayı Girin")
sayi.pack()

giris = Entry(window)
giris.pack()

buton = Button(window)
buton.config(text="Uygula")
buton.config(command=sayigir)
buton.pack()

window.mainloop()

