import json
from datetime import datetime


class Order:
    def __init__(self, order_id=0, bouquet=None, order_dict=None, user=None, address=None, order_date=None,
                 credit_card=None, bouquets=None):
        if order_dict is None:
            self.id = order_id
            self.bouquet = bouquet
            self.user = user
            self.address = address
            if order_date is not None:
                self.order_date = order_date
            else:
                self.order_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            self.credit_card = credit_card
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
        if 'address' in order_dict:
            self.address = order_dict['address']
        else:
            self.address = None
        if 'order_date' in order_dict:
            self.order_date = order_dict['order_date']
        else:
            self.order_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        if 'credit_card' in order_dict:
            self.credit_card = order_dict['credit_card']
        else:
            self.credit_card = None
        if 'bouquet' in order_dict:
            for bouquet in bouquets:
                if bouquet.id == order_dict['bouquet']:
                    self.bouquet = bouquet
                    break
        else:
            self.bouquet = None

    def to_dict(self):
        return {'id': self.id, 'user': self.user, 'bouquet': self.bouquet.id, 'credit_card': self.credit_card,
                'address': self.address, 'order_date': self.order_date}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
