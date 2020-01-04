from tkinter import *
from PIL import ImageTk, Image
from LoginFrame import LoginFrame
from RegisterFrame import RegisterFrame
from InfoFrame import InfoFrame


class MainFrame(Frame):
    def __init__(self, root=None, data=None, ncols=None, nrows=None):
        Frame.__init__(self, root)
        self.root = root
        self.ncols = ncols
        if ncols is None:
            self.ncols = 4
        self.nrows = nrows
        if nrows is None:
            self.nrows = 3
        self.frames = []
        self.flower_shop = data
        self.login_dialog = None
        self.register_dialog = None
        self.info_dialog = None
        self.start = 0
        self.page = 0
        self.pages = 0
        self.init_main_frame()

    def init_main_frame(self):
        self.root.title(self.flower_shop.name)
        #self.root.configure(background="azure")
        self.root.columnconfigure(tuple(range(0, self.ncols)), weight=1)
        self.root.rowconfigure(tuple(range(0, self.nrows)), weight=1)
        for row in range(0, self.nrows):
            for col in range(0, self.ncols):
                frame = Frame(self.root)
                frame.grid(row=row, column=col, padx=5, pady=5)
                self.frames.append(frame)
        self.pages = int((len(self.flower_shop.bouquets) + 1) / (self.ncols * self.nrows))
        self.display_menu()

    def display_bouquet(self, bouquet, frame_index):
        Label(self.frames[frame_index], text=bouquet.name).pack()
        img = Image.open("../photos/"+bouquet.image)
        img = img.resize((130, 130), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label = Label(self.frames[frame_index], image=img)
        label.image = img
        label.pack()
        Label(self.frames[frame_index], text='Price: '+str(bouquet.price)+"€").pack()
        if self.flower_shop.logged_user is not None:
            Button(self.frames[frame_index], text="Buy", bg="RosyBrown2", width="12", height="1",
                   command=lambda: bouquet.buy()).pack()

    def display_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        info = Menu(menu)
        menu.add_cascade(label="Home")
        menu.add_cascade(label="Flowers")
        menu.add_cascade(label="Bouquets")
        info.add_command(label="Contact Us", command=self.information)
        menu.add_cascade(label="Info", menu=info)
        view = Menu(menu)
        menu.add_cascade(label="View", menu=view)
        view.add_command(label="2 x 2", command=lambda: self.change_grid(2, 2))
        view.add_command(label="3 x 2", command=lambda: self.change_grid(3, 2))
        view.add_command(label="4 x 3", command=lambda: self.change_grid(4, 3))
        view.add_command(label="5 x 3", command=lambda: self.change_grid(5, 3))
        user = Menu(menu)
        if self.flower_shop.logged_user is None:
            menu.add_cascade(label="User", menu=user)
            user.add_command(label="Login", command=self.login)
            user.add_command(label="Register", command=self.register)
        else:
            menu.add_cascade(label=self.flower_shop.logged_user.username, menu=user)
            user.add_command(label="Log out", command=self.logout)
        for frame in self.frames:
            for widget in frame.winfo_children():
                widget.destroy()
        j = 0
        for i in range(self.start, self.start+self.nrows*self.ncols-1):
            if i >= len(self.flower_shop.bouquets):
                break
            j = i
            self.display_bouquet(self.flower_shop.bouquets[i], i-self.start)
        if self.flower_shop.logged_user is not None:
            Button(self.frames[j-self.start+1], text="Create bouquet", bg="RosyBrown2", width="12", height="1").pack()
        if self.page > 0:
            Button(self.frames[j - self.start+1], text="Previous Page", bg="RosyBrown2", width="12", height="1",
                   command=lambda: self.previous_page()).pack()
        if self.page < self.pages and len(self.flower_shop.bouquets) >= self.ncols*self.nrows:
            Button(self.frames[j - self.start+1], text="Next Page", bg="RosyBrown2", width="12", height="1",
                   command=lambda: self.next_page()).pack()

    def login(self):
        self.login_dialog = Toplevel()
        self.login_dialog.geometry("400x300")
        self.login_dialog.focus_force()
        self.login_dialog.attributes('-topmost', 'true')
        self.root.attributes('-disabled', 'true')
        LoginFrame(root=self.login_dialog, parent=self, data=self.flower_shop)

    def register(self):
        self.register_dialog = Toplevel()
        self.register_dialog.geometry("400x300")
        self.register_dialog.focus_force()
        self.register_dialog.attributes('-topmost', 'true')
        self.root.attributes('-disabled', 'true')
        RegisterFrame(root=self.register_dialog, parent=self, data=self.flower_shop)

    def on_successful_login(self):
        print(self.flower_shop.to_json())
        self.login_dialog.destroy()
        self.root.attributes('-disabled', 'false')
        self.root.focus_force()
        self.display_menu()

    def on_successful_register(self):
        print(self.flower_shop.to_json())
        self.flower_shop.save('../flower_shop.json')
        self.register_dialog.destroy()
        self.root.attributes('-disabled', 'false')
        self.root.focus_force()
        self.display_menu()

    def information(self):
        self.info_dialog = Toplevel()
        self.info_dialog.geometry("200x90")
        self.info_dialog.focus_force()
        self.info_dialog.attributes('-topmost', 'true')
        self.root.attributes('-disabled', 'true')
        InfoFrame(root=self.info_dialog, parent=self)

    def logout(self):
        self.flower_shop.logged_user = None
        self.display_menu()

    def change_grid(self, ncols, nrows):
        print("changing grid to "+str(ncols)+"x"+str(nrows))
        self.frames = []
        self.ncols = ncols
        self.nrows = nrows
        for widget in self.root.winfo_children():
            widget.destroy()
        self.page = 0
        self.start = 0
        self.init_main_frame()

    def next_page(self):
        self.page += 1
        self.start = self.start + self.nrows*self.ncols - 1
        self.display_menu()

    def previous_page(self):
        self.page -= 1
        self.start = self.start - self.nrows*self.ncols + 1
        self.display_menu()
