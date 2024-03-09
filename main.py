import tkinter as tk

def is_palindrome():
    if var.get() == 1:
        txt = ent_text.get().lower()
        if txt == "":
            lbl_txt.config(text="Please Enter a Word", bg="Cyan")
        else:
            if txt == txt[::-1]:
                lbl_txt.config(text="Palindrome", bg="Green")
            else:
                lbl_txt.config(text="Not a Palindrome", bg="Red", fg="White")
    elif var.get() == 2:
        txt = ent_text.get().lower()
        cleaned_txt = txt.split()
        fin_Txt = "".join(cleaned_txt)

        if fin_Txt == "":
            lbl_txt.config(text="Please Enter a Sentence", bg="Cyan")
        else:
            if fin_Txt == fin_Txt[::-1]:
                lbl_txt.config(text="Palindrome", bg="Green")
            else:
                lbl_txt.config(text="Not a Palindrome", bg="Red", fg="White")
    else:
        lbl_txt.config(text="Please Select Options", bg="Cyan")


#win Config
win = tk.Tk()
win.title("Palindrome Checker")
win.geometry("300x200")
win.resizable(False, False)
win.config(bg="#D6A184")

#widgets
ent_text = tk.Entry(win, width=20, font=("Helvetica", 16))
ent_text.pack(pady=10)

var = tk.IntVar()
r1 = tk.Radiobutton(win, 
                    text="Word", 
                    variable=var, 
                    value=1, 
                    bg="#D6A184", 
                    activebackground="#D6A184",
                    font=("Helvetica", 11)).pack()

r2 = tk.Radiobutton(win,
                    text="Sentence", 
                    variable=var, 
                    value=2, 
                    bg="#D6A184",
                    activebackground="#D6A184",
                    font=("Helvetica", 11)).pack()

btn_enter = tk.Button(win, text="Enter", font=("Helvetica", 12), command=is_palindrome, width=10).pack(pady=10)

lbl_txt = tk.Label(win, text="Palindrome or Not?", font=("Helvetica", 14))
lbl_txt.pack(pady=10)

win.mainloop()