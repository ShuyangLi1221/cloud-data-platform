from enum import Enum

class OrderStatus(str, Enum):
    OPEN = "open"
    WON = "won"
    LOST = "lost"