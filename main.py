import tkinter as tk

def is_palindrome():
    txt = ent_text.get().lower()
    if txt == "":
        pass
    else:
        if txt == txt[::-1]:
            lbl_txt.config(text="Palindrome", bg="Green")
        else:
            lbl_txt.config(text="Not a Palindrome", bg="Red", fg="White")



#win Config
win = tk.Tk()
win.title("Palindrome Checker")
win.geometry("300x200")
win.resizable(False, False)
win.config(bg="#D6A184")

#widgets
ent_text = tk.Entry(win, width=20, font=("Helvetica", 16))
ent_text.pack(pady=20)

btn_enter = tk.Button(win, text="Enter", font=("Helvetica", 12), command=is_palindrome, width=10).pack()

lbl_txt = tk.Label(win, text="Palindrome or Not?", font=("Helvetica", 14))
lbl_txt.pack(pady=20)

win.mainloop()