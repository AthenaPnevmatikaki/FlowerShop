from tkinter import *
import os
from Flower import Flower
from User import User
from Bouquet import Bouquet
from Order import Order
from FlowerShop import FlowerShop
from MainFrame import MainFrame


def initialise_flower_shop():
    flower = Flower(flower_dict={'type': 'Rose', 'color': 'Red', 'name': 'King Edward red rose', 'price': 4.5,
                                 'image': 'king_Edward_red_rose.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Carnation', 'color': 'Red', 'name': 'Red carnation', 'price': 2.5,
                                 'image': 'red_carnation.jpg'})
    flower_shop.add_flower(flower)
    bouquet = Bouquet(bouquet_dict={'name': 'Red rose & carnations', 'flowers': [1, 1, 1, 1, 1, 1, 2, 2, 2],
                                    'image': 'red_roses_carnations.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    user = User(user_dict={'email': 'a.pnevmatikaki@gmail.com', 'password': '1234', 'username': 'apne'})
    flower_shop.add_user(user)
    order = Order(order_dict={'user': 1, 'bouquet': 1}, bouquets=flower_shop.bouquets)
    flower_shop.add_order(order)
    flower_shop.save('../flower_shop.json')


flower_shop = FlowerShop("Το Λέλουδο", [], [], [], [])
if os.path.exists('../flower_shop.json'):
    print('Loading flower shop data')
    flower_shop.load('../flower_shop.json')
else:
    print('Initialising flower shop')
    initialise_flower_shop()
print(flower_shop.to_json())
print(f'\nBouquet {flower_shop.bouquets[0].name} costs {flower_shop.bouquets[0].price}')

root = Tk()
root.geometry("1200x700+300+0")
app = MainFrame(root=root, data=flower_shop)
root.mainloop()
