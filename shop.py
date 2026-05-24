class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0
    def describe_shop(self):
        print(f"Shop name: {self.shop_name}")
        print(f"Store type: {self.store_type}")
    def open_shop(self):
        print(f"The shop {self.shop_name} is now open!")
    def set_number_of_units(self, n):
        self.number_of_units = n
    def increment_number_of_units(self, n):
        self.number_of_units += n

store = Shop("Lidl", "grocery")
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()
print(store.number_of_units)
store.number_of_units = 50
print(store.number_of_units)

store.set_number_of_units(100)
print(store.number_of_units)

store.increment_number_of_units(25)
print(store.number_of_units)


shop_2 = Shop("Metro", "wholesale")
shop_2.describe_shop()

shop_3 = Shop("SILPO", "supermarket")
shop_3.describe_shop()

shop_4 = Shop("ATB","discounter")
shop_4.describe_shop()

class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discount_products(self):
        print(self.discount_products)

store_discount = Discount("Lidl", "grocery")
store_discount.discount_products = ["milk", "bread", "eggs"]
store_discount.get_discount_products()