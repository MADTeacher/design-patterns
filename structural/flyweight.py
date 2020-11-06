class PizzaOrderFlyWeight:

    def __init__(self, shared_state):
        self.shared_state = shared_state

    def __repr__(self):
        return str(self.shared_state)


class PizzaOrderContext:

    def __init__(self, unique_state, flyweight: PizzaOrderFlyWeight):
        self.unique_state = unique_state
        self.flyweight = flyweight

    def __repr__(self):
        return f"уникальное состояние: {self.unique_state} \n" \
               f"разделяемое состояние: {self.flyweight}"


class FlyWeightFactory:

    def __init__(self):
        self.flyweights = []

    def get_flyweight(self, shared_state) -> PizzaOrderFlyWeight:

        flyweights = list(filter(lambda x: x.shared_state ==
                                           shared_state, self.flyweights))
        if flyweights:
            return flyweights[0]
        else:
            flyweight = PizzaOrderFlyWeight(shared_state)
            self.flyweights.append(flyweight)
            return flyweight

    @property
    def total(self):
        return len(self.flyweights)


class PizzaOrderMaker:

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.contexts = []

    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        context = PizzaOrderContext(unique_state, flyweight)
        self.contexts.append(context)

        return context


if __name__ == "__main__":
    flyweight_factory = FlyWeightFactory()
    pizza_maker = PizzaOrderMaker(flyweight_factory)

    shared_states = [(30, 'Большая пицца'),
                     (25, 'Средняя пицца'),
                     (10, 'Маленькая пицца')]
    unique_states = ['Маргарита', 'Салями', '4 сыра']

    orders = [pizza_maker.make_pizza_order(x, y)
              for x in unique_states
              for y in shared_states]

    print("Количество созданных пицц:", len(orders))
    print("Количество разделяемых объектов:", flyweight_factory.total)
    for index, pizza in enumerate(orders):
        print("-"*20)
        print(f"Номер пиццы в списке: {index}")
        print(pizza)
