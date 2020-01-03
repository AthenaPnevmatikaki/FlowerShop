import json


class Bouquet:
    def __init__(self, bouquet_id=0, name=None, flowers=None, image=None, bouquet_dict=None):
        if bouquet_dict is None:
            self.id = bouquet_id
            self.name = name
            self.flowers = flowers
            self.image = image
            self.price = 0
            if flowers is not None:
                for flower in flowers:
                    self.price += flower.price
        else:
            self.from_dict(bouquet_dict, flowers)

    def from_dict(self, bouquet_dict, flowers):
        if 'id' in bouquet_dict:
            self.id = bouquet_dict['id']
        else:
            self.id = 0
        if 'name' in bouquet_dict:
            self.name = bouquet_dict['name']
        else:
            self.name = None
        if 'image' in bouquet_dict:
            self.image = bouquet_dict['image']
        else:
            self.image = None
        self.price = 0
        if 'flowers' in bouquet_dict:
            self.flowers = []
            for flower_id in bouquet_dict['flowers']:
                for flower in flowers:
                    if flower.id == flower_id:
                        self.flowers.append(flower)
                        self.price += flower.price
                        break
        else:
            self.flowers = None

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'flowers': [flower.id for flower in self.flowers],
                'image': self.image}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)

    def buy(self):
        print("Buying the "+self.name)
