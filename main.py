from tkinter import *
from tkinter import messagebox

def enkripsi(text, shift):
    result = ""

    for x in range(len(text)):
        char = text[x]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def dekripsi(text, shift):
    result = ""

    for x in range(len(text)):
        char = text[x]

        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char

    return result

def halaman_utama():

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")

    screen.title("5200411193_Pramadika Egamo")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    def encrypt_text():
        text = text1.get("1.0", END)
        shift = int(code.get())
        encrypted_text = enkripsi(text.strip(), shift)
        messagebox.showinfo("Hasil Enkripsi", encrypted_text)

    def decrypt_text():
        text = text1.get("1.0", END)
        shift = int(code.get())
        decrypted_text = dekripsi(text.strip(), shift)
        messagebox.showinfo("Hasil Dekripsi", decrypted_text)

    Label(text="Masukan teks untuk enkripsi dan dekripsi", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0, height=5)
    text1.place(x=10, y=50, width=355)

    Label(text="Masukan kunci rahasia untuk enkripsi dan deskripsi", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial,25"), show="*").place(x=10, y=200)

    Button(text="ENKRIPSI", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt_text).place(x=10, y=250)
    Button(text="DEKRIPSI", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt_text).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

if __name__ == "__main__":
    halaman_utama()
