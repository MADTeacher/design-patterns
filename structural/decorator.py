from abc import ABC, abstractmethod


class IPizzaBase(ABC):
    """Интерфейс декорируемого объекта"""
    @abstractmethod
    def cost(self) -> float:
        pass


class PizzaBase(IPizzaBase):
    """Класс декорируемого объекта"""
    def __init__(self, cost):
        self.__cost = cost

    def cost(self) -> float:
        return self.__cost


class IDecorator(IPizzaBase):
    """Интерфейс декоратора"""
    @abstractmethod
    def name(self) -> str:
        pass


class PizzaMargarita(IDecorator):
    """На основе PizzaBase получаем
    пиццу 'Маргарита'"""
    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Маргарита"

    def cost(self) -> float:
        return self.__cost+self.__wrapped.cost()

    def name(self) -> str:
        return self.__name


class PizzaSalami(IDecorator):
    """На основе PizzaBase получаем
    пиццу 'Салями'"""
    def __init__(self, wrapped: IPizzaBase, pizza_cost: float):
        self.__wrapped = wrapped
        self.__cost = pizza_cost
        self.__name = "Салями"

    def cost(self) -> float:
        return (self.__cost+self.__wrapped.cost())*2

    def name(self) -> str:
        return self.__name


if __name__ == "__main__":
    def print_pizza(pizza: IDecorator) -> None:
        print(f"Стоимость пиццы '{pizza.name()}' = {pizza.cost()}")

    pizza_base = PizzaBase(3.4)
    print(f"Стоимость основы пиццы = {pizza_base.cost()}")
    margarita = PizzaMargarita(pizza_base, 10)
    print_pizza(margarita)
    salami = PizzaSalami(pizza_base, 7)
    print_pizza(salami)