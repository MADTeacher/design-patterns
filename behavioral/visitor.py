from abc import ABC, abstractmethod
from typing import List


class OrderItemVisitor(ABC):
    """Интерфейс посетителя"""
    @abstractmethod
    def visit(self, item) -> float:
        ...


class ItemElement(ABC):
    """Интерфейс для заказываемых продуктов"""
    @abstractmethod
    def accept(self, visitor) -> OrderItemVisitor:
        ...


class Pizza(ItemElement):
    """Класс заказываемой пиццы"""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor) -> OrderItemVisitor:
        return visitor.visit(self)


class Coffee(ItemElement):
    """Класс заказываемого кофе"""
    def __init__(self, name: str,
                 price: float,
                 capacity: float):
        self.name = name
        self.price = price  # цена за литр кофе)
        self.capacity = capacity

    def get_price(self) -> float:
        return self.price

    def get_capacity(self) -> float:
        return self.capacity

    def accept(self, visitor) -> OrderItemVisitor:
        return visitor.visit(self)


class WithOutDiscountVisitor(OrderItemVisitor):
    """Посчитываем сумму заказа с
    без учета скидки"""
    def visit(self, item) -> float:
        cost = 0
        if isinstance(item, Pizza):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost


class OnlyPizzaDiscountVisitor(OrderItemVisitor):
    """Посчитываем сумму заказа с
    учетом скидки на всю пиццу в 15%"""
    def visit(self, item) -> float:
        cost = 0
        if isinstance(item, Pizza):
            cost = item.get_price()
            cost -= cost * 0.15
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost


class OnlyCoffeeDiscountVisitor(OrderItemVisitor):
    """Посчитываем сумму заказа с
    учетом скидки на всё кофе в 35%"""
    def visit(self, item) -> float:
        cost = 0
        if isinstance(item, Pizza):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
            cost -= cost * 0.35
        return cost


class AllDiscountVisitor(OrderItemVisitor):
    """Посчитываем сумму заказа с
    учетом скидки на всё в 20"""
    def visit(self, item) -> float:
        cost = 0
        if isinstance(item, Pizza):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        cost -= cost * 0.20
        return cost


class Waiter:
    def __init__(self, discount: OrderItemVisitor):
        self.order: List[ItemElement] = []
        self.discount_calculator = discount

    def set_order(self, order: List[ItemElement]) -> None:
        self.order = order

    def set_discount(self, discount: OrderItemVisitor) -> None:
        self.discount_calculator = discount

    def calculate_finish_price(self) -> float:
        price = 0
        if self.order:
            for item in self.order:
                price += item.accept(self.discount_calculator)
        return price


if __name__ == "__main__":
    order: List[ItemElement] = [Pizza("Маргарита", 12.3),
                                Coffee("Латте", 5, 0.3),
                                Pizza("4Сыра", 10.5),
                                Pizza("Салями", 15.2),
                                Coffee("Капучино", 4, 0.27)]
    discount = WithOutDiscountVisitor()
    waiter = Waiter(discount)
    waiter.set_order(order)
    print(f"Сумма заказа без учета скидок: "
          f"{waiter.calculate_finish_price()}")
    discount = OnlyPizzaDiscountVisitor()
    waiter.set_discount(discount)
    print(f"Сумма заказа c учетом скидки на пиццу: "
          f"{waiter.calculate_finish_price()}")
    discount = OnlyCoffeeDiscountVisitor()
    waiter.set_discount(discount)
    print(f"Сумма заказа c учетом скидки на коффе: "
          f"{waiter.calculate_finish_price()}")
    discount = AllDiscountVisitor()
    waiter.set_discount(discount)
    print(f"Сумма заказа c учетом скидки на всё: "
          f"{waiter.calculate_finish_price()}")