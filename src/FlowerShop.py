import json
from Flower import Flower
from Bouquet import Bouquet
from User import User
from Order import Order


class FlowerShop:
    def __init__(self, name, flowers, bouquets, users, orders):
        self.name = name
        self.flowers = flowers
        self.bouquets = bouquets
        self.users = users
        self.orders = orders
        self.logged_user = None
        self.orders_id_counter = len(self.orders)
        self.users_id_counter = len(self.users)
        self.flowers_id_counter = len(self.flowers)
        self.bouquets_id_counter = len(self.bouquets)

    def from_dict(self, flower_shop_dict):
        self.logged_user = None
        self.name = ""
        if 'name' in flower_shop_dict:
            self.name = flower_shop_dict['name']
        self.flowers = []
        if 'flowers' in flower_shop_dict:
            for flower_dict in flower_shop_dict['flowers']:
                flower = Flower()
                flower.from_dict(flower_dict)
                self.flowers.append(flower)
        self.bouquets = []
        if 'bouquets' in flower_shop_dict:
            for bouquet_dict in flower_shop_dict['bouquets']:
                bouquet = Bouquet()
                bouquet.from_dict(bouquet_dict, self.flowers)
                self.bouquets.append(bouquet)
        self.users = []
        if 'users' in flower_shop_dict:
            for user_dict in flower_shop_dict['users']:
                user = User()
                user.from_dict(user_dict)
                self.users.append(user)
        self.orders = []
        if 'orders' in flower_shop_dict:
            for order_dict in flower_shop_dict['orders']:
                order = Order()
                order.from_dict(order_dict, self.bouquets)
                self.orders.append(order)
        self.orders_id_counter = len(self.orders)
        self.users_id_counter = len(self.users)
        self.flowers_id_counter = len(self.flowers)
        self.bouquets_id_counter = len(self.bouquets)
        self.logged_user = self.users[0]     #TODO: remove this line

    def to_dict(self):
        if self.logged_user is None:
            logged_user = None
        else:
            logged_user = self.logged_user.to_dict()
        flowers = []
        for flower in self.flowers:
            flowers.append(flower.to_dict())
        bouquets = []
        for bouquet in self.bouquets:
            bouquets.append(bouquet.to_dict())
        users = []
        for user in self.users:
            users.append(user.to_dict())
        orders = []
        for order in self.orders:
            orders.append((order.to_dict()))
        return {'name': self.name, 'logged_user': logged_user,
                'flowers_id_counter': self.flowers_id_counter, 'flowers': flowers,
                'bouquets_id_counter': self.bouquets_id_counter, 'bouquets': bouquets,
                'users_id_counter': self.users_id_counter, 'users': users,
                'orders_id_counter': self.orders_id_counter, 'orders': orders}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)

    def save(self, filename):
        with open(filename, 'w') as outfile:
            json.dump(self.to_dict(), outfile, indent=4, ensure_ascii=False)

    def load(self, filename):
        with open(filename, 'r') as json_file:
            flower_shop_dict = json.load(json_file)
            self.from_dict(flower_shop_dict)

    def add_flower(self, flower):
        self.flowers_id_counter += 1
        flower.id = self.flowers_id_counter
        self.flowers.append(flower)

    def add_bouquet(self, bouquet):
        self.bouquets_id_counter += 1
        bouquet.id = self.bouquets_id_counter
        self.bouquets.append(bouquet)

    def add_user(self, user):
        user_already_exists = False
        for existing_user in self.users:
            if existing_user.username == user.username:
                user_already_exists = True
                break
        if user_already_exists:
            return False
        else:
            self.users_id_counter += 1
            user.id = self.users_id_counter
            self.users.append(user)
            return True

    def add_order(self, order):
        self.orders_id_counter += 1
        order.id = self.orders_id_counter
        self.orders.append(order)
