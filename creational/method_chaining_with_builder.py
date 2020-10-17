from creational.builder_with_director import (PizzaSauceType,
                                              PizzaBase,
                                              PizzaDoughDepth,
                                              PizzaDoughType,
                                              PizzaTopLevelType)
"""
Класс компонуемого продукта
"""


class Pizza:
    def __init__(self, builder):
        self.name = builder.name
        self.dough = builder.dough
        self.sauce = builder.sauce
        self.topping = builder.topping
        self.cooking_time = builder.cooking_time  # in minute

    def __str__(self):
        info: str = f"Pizza name: {self.name} \n" \
                    f"dough type: {self.dough.DoughDepth.name} & " \
                    f"{self.dough.DoughType.name}\n" \
                    f"sauce type: {self.sauce} \n" \
                    f"topping: {[it.name for it in self.topping]} \n" \
                    f"cooking time: {self.cooking_time} minutes"
        return info

    @staticmethod
    def getBuilder():
        return _Builder()


"""
Реализация строителя (шеф-поваров) для сборки пицц c использованием паттерна Method Chaining
"""


class _Builder:
    def set_name(self, name: str):
        self.name = name
        return self

    def set_dough(self, pizza_base: PizzaBase):
        self.dough = pizza_base
        return self

    def set_sauce(self, sauce: PizzaSauceType):
        self.sauce = sauce
        return self

    def set_topping(self, topping: list):
        self.topping = topping
        return self

    def set_cooking_time(self, time: int):
        self.cooking_time = time
        return self

    def build(self):
        return Pizza(self)


if __name__ == "__main__":
    # Готовим пиццу Маргарита
    pizza_base = PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT)
    pizza = Pizza.getBuilder().\
        set_name("Margarita")\
        .set_dough(pizza_base)\
        .set_sauce(PizzaSauceType.TOMATO)\
        .set_topping(
            [
                it for it in (PizzaTopLevelType.MOZZARELLA,
                              PizzaTopLevelType.MOZZARELLA,
                              PizzaTopLevelType.BACON,
                              )
            ])\
        .set_cooking_time(10)\
        .build()
    print(pizza)
