import json


class User:
    def __init__(self, user_id=0, email=None, password=None, user_dict=None):
        if user_dict is None:
            self.id = user_id
            self.email = email
            self.password = password
        else:
            self.from_dict(user_dict)

    def from_dict(self, user_dict):
        if 'id' in user_dict:
            self.id = user_dict['id']
        else:
            self.id = 0
        if 'email' in user_dict:
            self.email = user_dict['email']
        else:
            self.email = None
        if 'password' in user_dict:
            self.password = user_dict['password']
        else:
            self.password = None

    def to_dict(self):
        return {'id': self.id, 'email': self.email, 'password': self.password}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)

