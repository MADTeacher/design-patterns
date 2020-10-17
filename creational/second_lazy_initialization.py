from typing import List

from creational.builder_with_director import (PizzaSauceType,
                                              PizzaBase,
                                              PizzaDoughDepth,
                                              PizzaDoughType,
                                              PizzaTopLevelType)

"""
Класс компонуемого продукта
"""


class Pizza:
    def __init__(self, pizza_name: str):
        self._name = pizza_name
        self._dough = PizzaBase(PizzaDoughDepth.THICK,
                                PizzaDoughType.WHEAT)
        self._sauce = None
        self._topping = None
        self._cooking_time = None  # in minute

    def __str__(self):
        info: str = f"Pizza name: {self._name} \n" \
                    f"dough type: {self._dough.DoughDepth.name} & " \
                    f"{self._dough.DoughType.name}\n"
        if self._sauce is None:
            self._lazy_default_sauce()
        info += f"sauce type: {self._sauce} \n"

        if self._topping is None:
            self._lazy_default_topping()
        info += f"topping: {[it.name for it in self._topping]} \n"

        if self._cooking_time is None:
            self._lazy_default_time()
        info += f"cooking time: {self._cooking_time} minutes \n" \
                f"-----------------------------------------"
        return info

    def _lazy_default_sauce(self) -> None:
        print('Sauce Lazy initialization')
        self._sauce = PizzaSauceType.PESTO

    def _lazy_default_topping(self) -> None:
        print('Topping Lazy initialization')
        self._topping = [PizzaTopLevelType.MOZZARELLA,
                         PizzaTopLevelType.MOZZARELLA,
                         PizzaTopLevelType.BACON]

    def _lazy_default_time(self) -> None:
        print('Cooking time Lazy initialization')
        self._cooking_time = 12

    def get_sauce(self) -> PizzaSauceType:
        if self._sauce is None:
            self._lazy_default_sauce()
        return self._sauce

    def get_name(self):
        return self._name

    def get_dough(self) -> PizzaBase:
        return self._dough

    def get_cooking_time(self) -> int:
        if self._cooking_time is None:
            self._lazy_default_time()
        return self._cooking_time

    def get_topping(self) -> List[PizzaTopLevelType]:
        if self._topping is None:
            self._lazy_default_topping()
        return self._topping


if __name__ == "__main__":
    my_pizza = Pizza("Pikolito")
    print(my_pizza)

    new_pizza = Pizza("Bambino")
    print(new_pizza.get_name())
    print(new_pizza.get_dough())
    print(new_pizza.get_topping())
