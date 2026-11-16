from enum import Enum

class ProductCategory(str, Enum):

    PHONE = "Phone"

    LAPTOP = "Laptop"

    TABLET = "Tablet"

    MONITOR = "Monitor"

    AUDIO = "Audio"

    CAMERA = "Camera"

    GAMING = "Gaming"

    NETWORKING = "Networking"

    ACCESSORY = "Accessory"