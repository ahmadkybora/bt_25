from orator import Model


class User(Model):
    __fillable__ = [
        'user_id',
        'username',
        'name',
        'age',
        'coin'
    ]
