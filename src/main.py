from tkinter import *
import os
from Flower import Flower
from User import User
from Bouquet import Bouquet
from Order import Order
from FlowerShop import FlowerShop
from MainFrame import MainFrame


def initialise_flower_shop():
    flower = Flower(flower_dict={'type': 'Rose', 'color': 'Red', 'name': 'Red Rose', 'price': 4.5,
                                 'image': 'king_Edward_red_rose.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Carnation', 'color': 'Red', 'name': 'Red carnation', 'price': 2.5,
                                 'image': 'red_carnation.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Carnation', 'color': 'White', 'name': 'White carnation', 'price': 2.5,
                                 'image': 'White Carnation.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Carnation', 'color': 'Pink', 'name': 'Pink carnation', 'price': 2.5,
                                 'image': 'Pink Carnation.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Sunflower', 'color': 'Yellow', 'name': 'Sunflower', 'price': 3,
                                 'image': 'sunflower.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Lily', 'color': 'White', 'name': 'Lily', 'price': 5,
                                 'image': 'white_lily.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Iris', 'color': 'Purple', 'name': 'Iris', 'price': 3.5,
                                 'image': 'iris.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Hyacinth', 'color': 'Pink', 'name': 'Hyacinth', 'price': 4.5,
                                 'image': 'hyacinth.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Lavender', 'color': 'Purple', 'name': 'Lavender', 'price': 0.4,
                                 'image': 'Lavender.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Rose', 'color': 'White', 'name': 'White Rose', 'price': 4,
                                 'image': 'White_rose.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Rose', 'color': 'Pink', 'name': 'Pink Rose', 'price': 4,
                                 'image': 'pink rose.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Cala Lily', 'color': 'Blue', 'name': 'Blue Cala Lily', 'price': 5,
                                 'image': 'Blue_cala_lily.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Tulip', 'color': 'Pink', 'name': 'Pink Tulip', 'price': 4,
                                 'image': 'Tulip Pink.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Tulip', 'color': 'White', 'name': 'White Tulip', 'price': 4,
                                 'image': 'white_tulip.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Tulip', 'color': 'Yellow', 'name': 'Yellow Tulip', 'price': 4,
                                 'image': 'yellow tulip.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Snapdragon', 'color': 'Orange', 'name': 'Snapdragon', 'price': 3,
                                 'image': 'Snapdragon.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Magnolia', 'color': 'White', 'name': 'White Magnolia', 'price': 3,
                                 'image': 'white_magnolia.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Magnolia', 'color': 'Orange', 'name': 'Orange Magnolia', 'price': 3,
                                 'image': 'orange_magnolia.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Lily', 'color': 'Yellow', 'name': 'Yellow Lily', 'price': 3,
                                 'image': 'yellow_lily.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Chrysanthemum', 'color': 'Pink', 'name': 'Pink Chrysanthemum', 'price': 3,
                                 'image': 'pink_chrysanthemum.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Chrysanthemum', 'color': 'Orange', 'name': 'Orange Chrysanthemum', 'price': 3,
                                 'image': 'orange_chrysanthemum.jpg'})
    flower_shop.add_flower(flower)
    flower = Flower(flower_dict={'type': 'Chrysanthemum', 'color': 'White', 'name': 'White Chrysanthemum', 'price': 3,
                                 'image': 'white_chrysanthemum.jpg'})
    flower_shop.add_flower(flower)

    bouquet = Bouquet(bouquet_dict={'name': 'Red Rose & White Carnations', 'flowers': [1, 1, 1, 1, 1, 3, 3, 3, 3],
                                    'image': 'red_roses_carnations.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Sunflowers & Lilies', 'flowers': [5, 5, 5, 5, 6, 6, 6, 6, 6],
                                    'image': 'sunflowers_lilies.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Red Rose & Lilies', 'flowers': [1, 1, 1, 1, 1, 6, 6, 6, 6],
                                    'image': 'red_roses_lilies.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Sunflowers & Red Carnations', 'flowers': [5, 5, 5, 5, 2, 2, 2, 2, 2],
                                    'image': 'sunflowers_carnations.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Iris & Red Carnations', 'flowers': [5, 5, 5, 5, 2, 2, 2, 2, 2],
                                    'image': 'Iris_carnations.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Iris & White Lilies', 'flowers': [7, 7, 7, 7, 7, 6, 6, 6, 6],
                                    'image': 'iris_lilies.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Lila Fantasy', 'flowers': [8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 11, 11, 12, 12, 12],
                                    'image': 'White&Pink_roses_tulips_lavender.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Pink & White Carnations', 'flowers': [3, 3, 3, 3, 4, 4, 4, 4, 4],
                                    'image': 'Pink & white carnations.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Snapdragon compilation', 'flowers': [16, 16, 16, 16, 16, 16, 16, 16],
                                    'image': 'snapdragon_bouquet.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Magnolia compilation', 'flowers': [17, 17, 17, 17, 17, 17],
                                    'image': 'Magnolia_bouguet.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Yellow Delight', 'flowers': [5, 5, 5, 19, 19, 19, 16, 16, 16, 16, 16],
                                    'image': 'Yellow_delight.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(bouquet_dict={'name': 'Chrysanthemum Compilation', 'flowers': [22, 22, 22, 22, 22, 20, 20, 20, 20],
                                    'image': 'chrysanthemum_compilation.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)
    bouquet = Bouquet(
        bouquet_dict={'name': 'Wild Bloom', 'flowers': [21, 21, 21, 16, 16, 16, 3, 20, 20, 18, 18],
                      'image': 'wild_bloom.jpg'}, flowers=flower_shop.flowers)
    flower_shop.add_bouquet(bouquet)

    user = User(user_dict={'email': 'a.pnevmatikaki@gmail.com', 'password': '1234', 'username': 'apne'})
    flower_shop.add_user(user)
    order = Order(order_dict={'user': 1, 'bouquet': 1}, bouquets=flower_shop.bouquets)
    flower_shop.add_order(order)
    flower_shop.save('../flower_shop.json')


flower_shop = FlowerShop("Flower Shop", [], [], [], [])
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
app = MainFrame(root=root, data=flower_shop, ncols=5, nrows=3)
root.mainloop()
