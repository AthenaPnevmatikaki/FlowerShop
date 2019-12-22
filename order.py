import json

class Order:
    def __init__(self,order_id=0,flowers=None,bouquets=None,order_dict=None,user=None,name=None):
        if order_dict is None:
            self.id=order_id
            self.price=0
            self.flowers=flowers
            self.bouquets=bouquets
            self.user=user
            self.name=name
            if flowers is not None:
                for flower in flowers:
                    self.price += flower.price
            if bouquets is not None:
                for bouquet in bouquets:
                    self.price+= bouquet.price
        else:
            self.from_dict(item_dict, flowers,bouquets)

    def from_dict(self, item_dict, flowers,bouquets):
        if 'id' in item_dict:
            self.id = item_dict['id']
        else:
            self.id = 0
        if 'user' in item_dict:
            self.user = item_dict['user']
        else:
            self.user = None
        self.price = 0
        if 'flowers' in item_dict:
            self.flowers = []
            for flower_id in item_dict['flowers']:
                for flower in flowers:
                    if flower.id == flower_id:
                        self.flowers.append(flower)
                        self.price += flower.price
                        break
        else:
            self.flowers = None

        if 'bouquets' in item_dict:
            self.bouquets=[]
            for bouquet_id in item_dict['bouquets']:
                for flower in flowers:
                    if bouquet.id == bouquet_id:
                        self.bouquets.append(bouquet)
                        self.price += bouquet.price
                        break
        else:
            self.bouquets = None


    def to_dict(self):
        return {'id': self.id, 'user': self.user, 'flowers': [flower.id for flower in self.flowers],
                'bouquets': [bouquet.id for bouquet in self.bouquets]}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
