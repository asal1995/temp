from enum import Enum


class UserType(Enum):
    CUSTOMER = 'customer'
    SELLER = 'seller'

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
