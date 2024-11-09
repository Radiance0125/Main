import tkinter as tk


usrn = ""
psw = ""

cusrn = "raiden1234"
cpsw = "password0123"

def login():

    def submit_usrn():
        global usrn
        usrn = usrn_txt.get()
    
    def submit_psw():
        global psw
        psw = psw_txt.get()

    def submit_login():
        submit_psw()
        submit_usrn()
        root.destroy()

    root = tk.Tk()

    root.geometry("325x250")

    root.title("login")

    usrn_lbl = tk.Label(root, text = "username:", font = ("Arial", 16))
    usrn_lbl.pack(padx = 10, pady = 10)

    usrn_txt = tk.Entry(root, font = ("arial", 16))
    usrn_txt.pack(padx = 10, pady = 10)

    psw_lbl = tk.Label(root, text = "password:", font = ("Arial", 16))
    psw_lbl.pack(padx = 10, pady = 10)

    psw_txt = tk.Entry(root, font = ("arial", 16))
    psw_txt.pack(padx = 10, pady = 10)

    entrbtn = tk.Button(root, text = "enter", font = ("Arial", 16), command = lambda : submit_login())
    entrbtn.pack(padx = 10, pady = 10)

    root.mainloop()

login()

if psw == cpsw and usrn == cusrn:
    print("login sucessful")
else:
    print("incorrect username/password")

