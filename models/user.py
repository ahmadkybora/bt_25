from orator import Model


class User(Model):
    __fillable__ = [
        'user_id',
        'username',
        'first_name',
        'last_name',
        'age',
        'coin'
    ]
