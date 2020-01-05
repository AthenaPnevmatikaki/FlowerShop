from tkinter import *
from PIL import ImageTk, Image
from LoginFrame import LoginFrame
from RegisterFrame import RegisterFrame
from InfoFrame import InfoFrame
from OrderFrame import OrderFrame
from Bouquet import Bouquet
from Order import Order


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
        self.order_dialog = None
        self.start = 0
        self.page = 0
        self.pages = 0
        self.showing = "bouquets"
        self.flower_counters = [0] * len(self.flower_shop.flowers)
        self.flower_counter_labels = [Label()] * len(self.flower_shop.flowers)
        self.bouquet_name = StringVar()
        self.init_main_frame()

    def init_main_frame(self):
        self.root.title(self.flower_shop.name)
        self.root.columnconfigure(tuple(range(0, self.ncols)), weight=1)
        self.root.rowconfigure(tuple(range(0, self.nrows)), weight=1)
        for row in range(0, self.nrows):
            for col in range(0, self.ncols):
                frame = Frame(self.root)
                frame.grid(row=row, column=col, padx=5, pady=5)
                self.frames.append(frame)
        if self.showing == "bouquets":
            self.pages = int((len(self.flower_shop.bouquets) + 1) / (self.ncols * self.nrows))
        elif self.showing == "flowers":
            self.pages = int((len(self.flower_shop.flowers) + 1) / (self.ncols * self.nrows))
        self.display_menu()

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
        if self.showing == "bouquets":
            j = 0
            for i in range(self.start, self.start + self.nrows * self.ncols - 1):
                if i >= len(self.flower_shop.bouquets):
                    break
                j = i
                self.display_bouquet(self.flower_shop.bouquets[i], i - self.start)
            if self.flower_shop.logged_user is not None:
                Button(self.frames[j - self.start + 1], text="Create bouquet", bg="RosyBrown2", width="12", height="1",
                       command=lambda: self.create_bouquet()).grid(row=0, columnspan=2, pady=5)
            prev_button = Button(self.frames[j - self.start + 1], text="<", bg="RosyBrown2", width="4", height="1",
                                 command=lambda: self.previous_page())
            prev_button.grid(row=1, column=0)
            if self.page > 0:
                prev_button.config(state=NORMAL)
            else:
                prev_button.config(state=DISABLED)
            next_button = Button(self.frames[j - self.start + 1], text=">", bg="RosyBrown2", width="4", height="1",
                                 command=lambda: self.next_page())
            next_button.grid(row=1, column=1)
            if self.page < self.pages and len(self.flower_shop.bouquets) >= self.ncols * self.nrows:
                next_button.config(state=NORMAL)
            else:
                next_button.config(state=DISABLED)
        elif self.showing == "flowers":
            j = 0
            for i in range(self.start, self.start + self.nrows * self.ncols - 1):
                if i >= len(self.flower_shop.flowers):
                    break
                j = i
                self.display_flower(self.flower_shop.flowers[i], i - self.start)
            prev_button = Button(self.frames[j - self.start + 1], text="<", bg="RosyBrown2", width="4", height="1",
                                 command=lambda: self.previous_page())
            prev_button.grid(row=3, column=0)
            if self.page > 0:
                prev_button.config(state=NORMAL)
            else:
                prev_button.config(state=DISABLED)
            next_button = Button(self.frames[j - self.start + 1], text=">", bg="RosyBrown2", width="4", height="1",
                                 command=lambda: self.next_page())
            next_button.grid(row=3, column=1)
            if self.page < self.pages and len(self.flower_shop.flowers) >= self.ncols*self.nrows:
                next_button.config(state=NORMAL)
            else:
                next_button.config(state=DISABLED)
            Label(self.frames[j - self.start + 1], text="Bouquet Name:").grid(row=0, column=0, columnspan=2)
            Entry(self.frames[j - self.start + 1], textvariable=self.bouquet_name).grid(row=1, column=0, columnspan=2)
            Button(self.frames[j - self.start + 1], text="Create", bg="RosyBrown2", width="6", height="1",
                   command=lambda: self.confirm_bouquet()).grid(row=2, column=0, pady=5)
            Button(self.frames[j - self.start + 1], text="Cancel", bg="RosyBrown2", width="6", height="1",
                   command=lambda: self.cancel_bouquet()).grid(row=2, column=1, pady=5)

    def display_bouquet(self, bouquet, frame_index):
        Label(self.frames[frame_index], text=bouquet.name).pack()
        img = Image.open("../photos/" + bouquet.image)
        img = img.resize((130, 130), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label = Label(self.frames[frame_index], image=img)
        label.image = img
        label.pack()
        Label(self.frames[frame_index], text='Price: ' + str(bouquet.price) + "€").pack()
        if self.flower_shop.logged_user is not None:
            Button(self.frames[frame_index], text="Buy", bg="RosyBrown2", width="12", height="1",
                   command=lambda: self.buy_bouquet(bouquet)).pack()

    def display_flower(self, flower, frame_index):
        Label(self.frames[frame_index], text=flower.name).grid(row=0, columnspan=3)
        img = Image.open("../photos/" + flower.image)
        img = img.resize((130, 130), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label = Label(self.frames[frame_index], image=img)
        label.image = img
        label.grid(row=1, columnspan=3)
        Label(self.frames[frame_index], text='Price: ' + str(flower.price) + "€").grid(row=2, columnspan=3)
        Button(self.frames[frame_index], text="-", bg="RosyBrown2", width="3", height="1",
               command=lambda: self.decrease_flower(flower)).grid(row=3, column=0)
        self.flower_counter_labels[flower.id - 1] = Label(self.frames[frame_index], text='0')
        self.flower_counter_labels[flower.id - 1].grid(row=3, column=1)
        Button(self.frames[frame_index], text="+", bg="RosyBrown2", width="3", height="1",
               command=lambda: self.increase_flower(flower)).grid(row=3, column=2)

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
        self.login_dialog.destroy()
        self.root.attributes('-disabled', 'false')
        self.root.focus_force()
        self.display_menu()

    def on_successful_register(self):
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
        print("changing grid to " + str(ncols) + "x" + str(nrows))
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
        self.start = self.start + self.nrows * self.ncols - 1
        self.display_menu()

    def previous_page(self):
        self.page -= 1
        self.start = self.start - self.nrows * self.ncols + 1
        self.display_menu()

    def create_bouquet(self):
        self.frames = []
        self.showing = "flowers"
        for widget in self.root.winfo_children():
            widget.destroy()
        self.page = 0
        self.start = 0
        self.init_main_frame()

    def increase_flower(self, flower):
        self.flower_counters[flower.id - 1] += 1
        self.flower_counter_labels[flower.id - 1].config(text=str(self.flower_counters[flower.id - 1]))

    def decrease_flower(self, flower):
        if self.flower_counters[flower.id - 1] > 0:
            self.flower_counters[flower.id - 1] -= 1
            self.flower_counter_labels[flower.id - 1].config(text=str(self.flower_counters[flower.id - 1]))

    def cancel_bouquet(self):
        self.frames = []
        self.showing = "bouquets"
        for widget in self.root.winfo_children():
            widget.destroy()
        self.page = 0
        self.start = 0
        self.init_main_frame()

    def confirm_bouquet(self):
        flowers = []
        for i in range(0, len(self.flower_counters)):
            if self.flower_counters[i] > 0:
                flowers.extend([i + 1] * self.flower_counters[i])
        if len(flowers) != 0 and str(self.bouquet_name.get()) != '':
            new_bouquet = Bouquet(bouquet_dict={'name': str(self.bouquet_name.get()), 'flowers': flowers,
                                                'image': 'generic_bouquet.jpg'}, flowers=self.flower_shop.flowers)
            self.flower_shop.add_bouquet(new_bouquet)
            self.flower_shop.save('../flower_shop.json')
            self.bouquet_name.set("")
            self.cancel_bouquet()

    def buy_bouquet(self, bouquet):
        self.order_dialog = Toplevel()
        self.order_dialog.geometry("400x100")
        self.order_dialog.focus_force()
        self.order_dialog.attributes('-topmost', 'true')
        self.root.attributes('-disabled', 'true')
        OrderFrame(root=self.order_dialog, parent=self, data=self.flower_shop, bouquet_id=bouquet.id)

    def on_cancelled_buy(self):
        self.order_dialog.destroy()
        self.root.attributes('-disabled', 'false')
        self.root.focus_force()

    def on_confirmed_buy(self, bouquet_id, address, credit_card):
        address = str(address.get())
        credit_card = str(credit_card.get())
        if address != "" and credit_card != "":
            order = Order(order_dict={'user': self.flower_shop.logged_user.id, 'bouquet': bouquet_id,'address': address,
                                      'credit_card': credit_card}, bouquets=self.flower_shop.bouquets)
            self.flower_shop.add_order(order)
            self.flower_shop.save('../flower_shop.json')
        self.on_cancelled_buy()
