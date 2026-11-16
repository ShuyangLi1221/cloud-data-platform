from decimal import Decimal
import random
from faker import Faker
from sqlalchemy.orm import Session
from common.database import engine
from models.product import Product
from enums.product_category import ProductCategory

fake = Faker("en_CA")

PRODUCT_CATALOG = [
    # ---------------- Phone ----------------
    {
        "category": ProductCategory.PHONE,
        "brand": "Apple",
        "name": "iPhone 16",
        "sku": "APP-IP16",
        "price": 1299.99,
        "cost": 899.99,
    },
    {
        "category": ProductCategory.PHONE,
        "brand": "Apple",
        "name": "iPhone 16 Pro",
        "sku": "APP-IP16P",
        "price": 1599.99,
        "cost": 1099.99,
    },
    {
        "category": ProductCategory.PHONE,
        "brand": "Samsung",
        "name": "Galaxy S25",
        "sku": "SAM-S25",
        "price": 1199.99,
        "cost": 819.99,
    },
    {
        "category": ProductCategory.PHONE,
        "brand": "Samsung",
        "name": "Galaxy S25 Ultra",
        "sku": "SAM-S25U",
        "price": 1799.99,
        "cost": 1269.99,
    },
    {
        "category": ProductCategory.PHONE,
        "brand": "Google",
        "name": "Pixel 10 Pro",
        "sku": "GOO-P10P",
        "price": 1399.99,
        "cost": 969.99,
    },

    # ---------------- Laptop ----------------
    {
        "category": ProductCategory.LAPTOP,
        "brand": "Apple",
        "name": "MacBook Air M4",
        "sku": "APP-MBA-M4",
        "price": 1699.99,
        "cost": 1199.99,
    },
    {
        "category": ProductCategory.LAPTOP,
        "brand": "Apple",
        "name": "MacBook Pro 14",
        "sku": "APP-MBP14",
        "price": 2599.99,
        "cost": 1839.99,
    },
    {
        "category": ProductCategory.LAPTOP,
        "brand": "Dell",
        "name": "XPS 13",
        "sku": "DEL-XPS13",
        "price": 1899.99,
        "cost": 1329.99,
    },
    {
        "category": ProductCategory.LAPTOP,
        "brand": "Lenovo",
        "name": "ThinkPad X1 Carbon",
        "sku": "LEN-X1",
        "price": 2199.99,
        "cost": 1539.99,
    },
    {
        "category": ProductCategory.LAPTOP,
        "brand": "ASUS",
        "name": "ROG Zephyrus G16",
        "sku": "ASU-G16",
        "price": 2499.99,
        "cost": 1749.99,
    },

    # ---------------- Tablet ----------------
    {
        "category": ProductCategory.TABLET,
        "brand": "Apple",
        "name": "iPad Air",
        "sku": "APP-IPA",
        "price": 899.99,
        "cost": 629.99,
    },
    {
        "category": ProductCategory.TABLET,
        "brand": "Apple",
        "name": "iPad Pro 13",
        "sku": "APP-IPP13",
        "price": 1699.99,
        "cost": 1199.99,
    },
    {
        "category": ProductCategory.TABLET,
        "brand": "Samsung",
        "name": "Galaxy Tab S10 Ultra",
        "sku": "SAM-TABS10U",
        "price": 1499.99,
        "cost": 1049.99,
    },

    # ---------------- Monitor ----------------
    {
        "category": ProductCategory.MONITOR,
        "brand": "Dell",
        "name": "UltraSharp 32",
        "sku": "DEL-U3223",
        "price": 999.99,
        "cost": 699.99,
    },
    {
        "category": ProductCategory.MONITOR,
        "brand": "LG",
        "name": "UltraFine 5K",
        "sku": "LG-UF5K",
        "price": 1799.99,
        "cost": 1269.99,
    },
    {
        "category": ProductCategory.MONITOR,
        "brand": "Samsung",
        "name": "Smart Monitor M8",
        "sku": "SAM-M8",
        "price": 799.99,
        "cost": 559.99,
    },

    # ---------------- Audio ----------------
    {
        "category": ProductCategory.AUDIO,
        "brand": "Apple",
        "name": "AirPods Pro 2",
        "sku": "APP-APP2",
        "price": 329.99,
        "cost": 199.99,
    },
    {
        "category": ProductCategory.AUDIO,
        "brand": "Sony",
        "name": "WH-1000XM6",
        "sku": "SON-XM6",
        "price": 549.99,
        "cost": 379.99,
    },
    {
        "category": ProductCategory.AUDIO,
        "brand": "Bose",
        "name": "QuietComfort Ultra",
        "sku": "BOS-QCU",
        "price": 599.99,
        "cost": 419.99,
    },

    # ---------------- Camera ----------------
    {
        "category": ProductCategory.CAMERA,
        "brand": "Canon",
        "name": "EOS R8",
        "sku": "CAN-R8",
        "price": 2199.99,
        "cost": 1599.99,
    },
    {
        "category": ProductCategory.CAMERA,
        "brand": "Sony",
        "name": "Alpha A7 IV",
        "sku": "SON-A74",
        "price": 3299.99,
        "cost": 2399.99,
    },
    {
        "category": ProductCategory.CAMERA,
        "brand": "DJI",
        "name": "Osmo Pocket 4",
        "sku": "DJI-OP4",
        "price": 799.99,
        "cost": 559.99,
    },

    # ---------------- Gaming ----------------
    {
        "category": ProductCategory.GAMING,
        "brand": "Sony",
        "name": "PlayStation 5",
        "sku": "SON-PS5",
        "price": 649.99,
        "cost": 449.99,
    },
    {
        "category": ProductCategory.GAMING,
        "brand": "Microsoft",
        "name": "Xbox Series X",
        "sku": "MS-XSX",
        "price": 649.99,
        "cost": 459.99,
    },
    {
        "category": ProductCategory.GAMING,
        "brand": "Nintendo",
        "name": "Switch 2",
        "sku": "NIN-SW2",
        "price": 599.99,
        "cost": 419.99,
    },

    # ---------------- Networking ----------------
    {
        "category": ProductCategory.NETWORKING,
        "brand": "TP-Link",
        "name": "Deco XE75",
        "sku": "TPL-XE75",
        "price": 499.99,
        "cost": 349.99,
    },
    {
        "category": ProductCategory.NETWORKING,
        "brand": "TP-Link",
        "name": "Archer AXE75",
        "sku": "TPL-AXE75",
        "price": 249.99,
        "cost": 169.99,
    },

    # ---------------- Accessory ----------------
    {
        "category": ProductCategory.ACCESSORY,
        "brand": "Logitech",
        "name": "MX Master 3S",
        "sku": "LOG-MX3S",
        "price": 139.99,
        "cost": 79.99,
    },
    {
        "category": ProductCategory.ACCESSORY,
        "brand": "Logitech",
        "name": "MX Keys",
        "sku": "LOG-MXKEY",
        "price": 169.99,
        "cost": 99.99,
    },
    {
        "category": ProductCategory.ACCESSORY,
        "brand": "Anker",
        "name": "737 Power Bank",
        "sku": "ANK-737",
        "price": 199.99,
        "cost": 119.99,
    },
]

class ProductService:
    @staticmethod
    def seed():
        with Session(engine) as session:
            if session.query(Product).count() > 0:
                print("Product already created")
                return
            else:
                products = []

                for product in PRODUCT_CATALOG:
                    db_product = Product(
                        sku=product["sku"],
                        brand=product["brand"],
                        product_name=product["name"],
                        category=ProductCategory(product["category"]),
                        price=Decimal(str(product["price"])),
                        cost=Decimal(str(product["cost"])),
                    )
                    products.append(db_product)
                session.add_all(products)
                session.commit()
                print(f"{len(products)} products inserted.")
