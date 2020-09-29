

class Product:

    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price

    def get_info(self):
        return f"ID={self._id}, name={self._name}, price={self._price}"

    def __str__(self):
        return self.get_info()

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = new_price


cola_cola = Product(1, "Cola-Cola", 4.99)
print(cola_cola.get_info())
print(cola_cola)
print(cola_cola.get_price())
print(cola_cola._price)
cola_cola.set_price(5.99)
cola_cola._price = 10
print(cola_cola)
