from typing import List
from collections.abc import Iterable, Iterator


class PizzaItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"кусочек пиццы под номером: {self.number}"


class PizzaSliceIterator(Iterator):
    def __init__(self, pizza: List[PizzaItem],
                 reverse: bool = False):
        self._pizza = pizza
        self._index: int = -1 if reverse else 0
        self._reverse = reverse

    def __next__(self) -> PizzaItem:
        try:
            pizza_item = self._pizza[self._index]
            self._index += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return pizza_item


class PizzaAggregate(Iterable):
    def __init__(self, amount_slices: int = 10):
        self._slices = [PizzaItem(it+1) for it in range(amount_slices)]
        print(f"Приготовили пиццу и порезали "
              f"на {amount_slices} кусочков")

    def amount_slices(self) -> int:
        return len(self._slices)

    def __iter__(self) -> PizzaSliceIterator:
        return PizzaSliceIterator(self._slices)

    def get_reverse_iterator(self) -> PizzaSliceIterator:
        return PizzaSliceIterator(self._slices, True)


if __name__ == "__main__":
    pizza = PizzaAggregate(5)
    for item in pizza:
        print("Это " + str(item))
    print("*" * 8 + "Обход в обратную сторону" + "*"*8)
    iterator = pizza.get_reverse_iterator()
    for item in iterator:
        print("Это " + str(item))

