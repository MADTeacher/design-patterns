from abc import ABC, abstractmethod


class IProduct(ABC):
    """Интерфейс продуктов
    входящих в пиццу"""
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class Product(IProduct):
    """Класс продукта"""
    def __init__(self, name: str, cost: float):
        self.__cost = cost
        self.__name = name

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class CompoundProduct(IProduct):
    """Класс компонуемых продуктов"""
    def __init__(self, name: str):
        self.__name = name
        self.products = []

    def cost(self):
        cost = 0
        for it in self.products:
            cost += it.cost()
        return cost

    def name(self) -> str:
        return self.__name

    def add_product(self, product: IProduct):
        self.products.append(product)

    def remove_product(self, product: IProduct):
        self.products.remove(product)

    def clear(self):
        self.products = []


class Pizza(CompoundProduct):
    """Класс пиццы"""
    def __init__(self, name: str):
        super(Pizza, self).__init__(name)

    def cost(self):
        cost = 0
        for it in self.products:
            cost_it = it.cost()
            print(f"Стоимость '{it.name()}' = {cost_it} тугриков")
            cost += cost_it
        print(f"Стоимость пиццы '{self.name()}' = {cost} тугриков")
        return cost


if __name__ == "__main__":
    dough = CompoundProduct("тесто")
    dough.add_product(Product("мука", 3))
    dough.add_product(Product("яйцо", 2.3))
    dough.add_product(Product("соль", 1))
    dough.add_product(Product("сахар", 2.1))
    sauce = Product("Барбекю", 12.1)
    topping = CompoundProduct("топпинг")
    topping.add_product(Product("Дор блю", 14))
    topping.add_product(Product("Пармезан", 12.3))
    topping.add_product(Product("Моцарелла", 9.54))
    topping.add_product(Product("Маасдам", 7.27))
    pizza = Pizza("4 сыра")
    pizza.add_product(dough)
    pizza.add_product(sauce)
    pizza.add_product(topping)
    print(pizza.cost())