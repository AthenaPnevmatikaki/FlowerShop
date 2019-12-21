from tkinter import *
from Flower import Flower
from Bouquet import Bouquet
from User import User
from FlowerShop import FlowerShop
from MainFrame import MainFrame

flower_shop = FlowerShop("Athena's Flowers", [], [], []) #

flower = Flower(flower_dict={'type': 'Rose', 'color': 'Red', 'name': 'King Edward red rose', 'price': 4.5,
                             'image': 'king_Edward_red_rose.jpg'})
flower_shop.add_flower(flower)
flower = Flower(flower_dict={'type': 'Carnation', 'color': 'Red', 'name': 'Red carnation', 'price': 2.5,
                             'image': 'red_carnation.jpg'})
flower_shop.add_flower(flower)

bouquet = Bouquet(bouquet_dict={'name': 'Red rose & carnations', 'flowers': [1, 1, 1, 1, 1, 1, 2, 2, 2],
                                'image': 'red_roses_carnations.jpg'}, flowers=flower_shop.flowers)
flower_shop.add_bouquet(bouquet)
flower_shop.save('../athena_flowers.json')
flower_shop = FlowerShop("", [], [], [])  #
print('Empty flower shop')
print(flower_shop.to_json())
flower_shop.load('../athena_flowers.json')
print('\nLoaded flower shop')
print(flower_shop.to_json())
print(f'\nBouquet {flower_shop.bouquets[0].name} costs {flower_shop.bouquets[0].price}')

root = Tk()
root.geometry("1200x700+300+0")
app = MainFrame(root=root, data=flower_shop)
root.mainloop()

