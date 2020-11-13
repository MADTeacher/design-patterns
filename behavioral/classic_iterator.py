from abc import ABC, abstractmethod
from typing import List


class Item(ABC):
    ...


class PizzaItem(Item):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"кусочек пиццы под номером: {self.number}"


class Iterator(ABC):
    @abstractmethod
    def next(self) -> Item:
        ...

    @abstractmethod
    def has_next(self) -> bool:
        ...


class PizzaSliceIterator(Iterator):
    def __init__(self, pizza: List[PizzaItem]):
        self._pizza = pizza
        self._index = 0

    def next(self) -> Item:
        pizza_item = self._pizza[self._index]
        self._index += 1
        return pizza_item

    def has_next(self) -> bool:
        return False if self._index >= len(self._pizza) else True


class PizzaAggregate:
    def __init__(self, amount_slices: int = 10):
        self.slices = [PizzaItem(it+1) for it in range(amount_slices)]
        print(f"Приготовили пиццу и порезали "
              f"на {amount_slices} кусочков")

    def amount_slices(self) -> int:
        return len(self.slices)

    def iterator(self) -> Iterator:
        return PizzaSliceIterator(self.slices)


if __name__ == "__main__":
    pizza = PizzaAggregate(5)
    iterator = pizza.iterator()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))
    print("*"*20)
    iterator = pizza.iterator()
    iterator.next()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))
