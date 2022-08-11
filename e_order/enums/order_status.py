from enum import Enum


class OrderStatus(Enum):

    ORDERED = 'ORDERED'
    PENDING = 'PENDING'
    CANCELED = 'CANCELED'
