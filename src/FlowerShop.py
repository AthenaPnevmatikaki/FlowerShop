import json
from Flower import Flower
from Bouquet import Bouquet


class FlowerShop:
    def __init__(self, name, flowers, bouquets):
        self.name = name
        self.flowers = flowers
        self.bouquets = bouquets
        self.user = None
        self.flowers_id_counter = len(self.flowers)
        self.bouquets_id_counter = len(self.bouquets)

    def from_dict(self, flower_shop_dict):
        self.user = None
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
        self.flowers_id_counter = len(self.flowers)
        self.bouquets_id_counter = len(self.bouquets)

    def to_dict(self):
        flowers = []
        for flower in self.flowers:
            flowers.append(flower.to_dict())
        bouquets = []
        for bouquet in self.bouquets:
            bouquets.append(bouquet.to_dict())
        return {'name': self.name, 'user': self.user,
                'flowers_id_counter': self.flowers_id_counter, 'flowers': flowers,
                'bouquets_id_counter': self.bouquets_id_counter, 'bouquets': bouquets}

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
