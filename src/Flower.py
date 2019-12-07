import json


class Flower:
    def __init__(self, flower_id=0, flower_type=None, color=None, name=None, price=0, image=None, flower_dict=None):
        if flower_dict is None:
            self.id = flower_id
            self.type = flower_type
            self.color = color
            self.name = name
            self.price = price
            self.image = image
        else:
            self.from_dict(flower_dict)

    def from_dict(self, flower_dict):
        if 'id' in flower_dict:
            self.id = flower_dict['id']
        else:
            self.id = 0
        if 'type' in flower_dict:
            self.type = flower_dict['type']
        else:
            self.type = None
        if 'color' in flower_dict:
            self.color = flower_dict['color']
        else:
            self.color = None
        if 'name' in flower_dict:
            self.name = flower_dict['name']
        else:
            self.name = None
        if 'price' in flower_dict:
            self.price = flower_dict['price']
        else:
            self.price = 0
        if 'image' in flower_dict:
            self.image = flower_dict['image']
        else:
            self.image = None

    def to_dict(self):
        return {'id': self.id, 'type': self.type, 'color': self.color, 'name': self.name, 'price': self.price,
                'image': self.image}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
