class Pizza:
    def __init__(self, pizza_name: str):
        self.name = pizza_name

    def __str__(self):
        return self.name


class PizzaPlace:
    def __init__(self) -> None:
        self.pizzas = {}

    def get_pizza(self, pizza_name: str) -> Pizza:
        if pizza_name not in self.pizzas:
            self.pizzas[pizza_name] = Pizza(pizza_name)

        return self.pizzas[pizza_name]


if __name__ == '__main__':
    my_pizza_place = PizzaPlace()
    print(my_pizza_place.get_pizza('Margarita'))
    print(my_pizza_place.get_pizza('Salami'))
