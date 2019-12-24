from tkinter import *
import os

class LoginFrame(Frame):
    def __init__(self, root=None, parent=None, data=None):
        Frame.__init__(self, root)
        self.root = root
        self.parent = parent
        self.flower_shop = data
        self.init_login_frame()

    def init_login_frame(self):
        global  username_verify, password_verify, username_entry1, password_entry1
        self.root.title("Login")
        username_verify = StringVar()
        password_verify = StringVar()
        Label(self.root, text="Username").pack()
        username_entry1 = Entry(self.root, textvariable=username_verify)
        username_entry1.pack()
        Label(self.root, text="password").pack()
        password_entry1 = Entry(self.root, textvariable=password_verify)
        password_entry1.pack()
        Label(self.root, text="").pack()
        Button(self.root, text="Login", bg="red", width="12", height="1", command=lambda:self.login_verify()).pack()

    #def login(self):
        #print("Logged in")
        #self.flower_shop.user = "apne"
        #self.root.destroy()
        #self.parent.on_successful_login()

    def login_verify(self):
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_success()
            else:
                self.wrong_password()
        else:
            self.wrong_username()

    def delete2(self):
        screen3.destroy()

    def delete3(self):
        screen4.destroy()

    def delete4(self):
        screen5.destroy()

    def login_success(self):
        global screen3
        screen3 = Toplevel(self.root)
        screen3.title("success")
        screen3.geometry("150x100")
        Label(screen3, text="Επιτυχής σύνδεση").pack()
        Button(screen3, text="OK", command=lambda:self.delete2()).pack()

    def wrong_password(self):
        global screen4
        screen4 = Toplevel(self.root)
        screen4.title("success")
        screen4.geometry("150x100")
        Label(screen4, text="Λάθος κωδικός").pack()
        Button(screen4, text="OK", command=lambda:self.delete3()).pack()

    def wrong_username(self):
        global screen5
        screen5 = Toplevel(self.root)
        screen5.title("success")
        screen5.geometry("150x100")
        Label(screen5, text="Ο χρήστης δεν βρέθηκε").pack()
        Button(screen5, text="OK", command=lambda:self.delete4()).pack()