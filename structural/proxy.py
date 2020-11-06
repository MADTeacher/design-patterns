from abc import ABC, abstractmethod


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


class IOrder(ABC):
    @abstractmethod
    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        pass


class PizzaOrderMaker(IOrder):

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.contexts = []

    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        context = PizzaOrderContext(unique_state, flyweight)
        self.contexts.append(context)

        return context


class ProxyOrderMaker(IOrder):

    def __init__(self, real_subject: PizzaOrderMaker):
        self.__real_subject = real_subject

    def make_pizza_order(self, unique_state, shared_state) -> PizzaOrderContext:
        self.__logging(unique_state, shared_state)
        return self.__real_subject.make_pizza_order(unique_state, shared_state)

    def check_access(self) -> bool:
        print('Проверка готовности Proxy')
        return self.__real_subject is not None

    def __logging(self, unique_state, shared_state) -> None:
        print(f"----Логируемые данные заказа----\n"
              f"уникальное состояние: {unique_state} \n"
              f"разделяемое состояние: {shared_state}")


if __name__ == "__main__":
    flyweight_factory = FlyWeightFactory()
    pizza_maker = PizzaOrderMaker(flyweight_factory)
    log_proxy = ProxyOrderMaker(pizza_maker)

    shared_states = [(30, 'Большая пицца'),
                     (25, 'Средняя пицца'),
                     (10, 'Маленькая пицца')]
    unique_states = ['Маргарита', 'Салями', '4 сыра']

    orders = [log_proxy.make_pizza_order(x, y)
              for x in unique_states
              for y in shared_states]
    print("#"*20)
    print("Количество созданных пицц:", len(orders))
    print("Количество разделяемых объектов:", flyweight_factory.total)
