import json


class Order:
    def __init__(self, order_id=0, bouquet=None, order_dict=None, user=None, bouquets=None):
        if order_dict is None:
            self.id = order_id
            self.bouquet = bouquet
            self.user = user
        else:
            self.from_dict(order_dict, bouquets)

    def from_dict(self, order_dict, bouquets):
        if 'id' in order_dict:
            self.id = order_dict['id']
        else:
            self.id = 0
        if 'user' in order_dict:
            self.user = order_dict['user']
        else:
            self.user = None
        if 'bouquet' in order_dict:
            for bouquet in bouquets:
                if bouquet.id == order_dict['bouquet']:
                    self.bouquet = bouquet
                    break
        else:
            self.bouquet = None

    def to_dict(self):
        return {'id': self.id, 'user': self.user, 'bouquet': self.bouquet.id}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
