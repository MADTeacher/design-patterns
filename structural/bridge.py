from abc import ABC, abstractmethod
import time

class Pizza:
    """Класс приццы для приготовления"""
    def __init__(self, name: str, cook_time: int, temperature: int):
        self.name = name
        self.cook_time = cook_time
        self.cook_temperature = temperature
        self.__isCook = False

    def cook(self) -> None:
        self.__isCook = True

    def isCooked(self) -> bool:
        return self.__isCook


class IOvenImplementor(ABC):
    """Интерфейс для реализации печей различного типа"""
    @abstractmethod
    def warm_up(self, temperature: int) -> None:
        pass

    @abstractmethod
    def cool_down(self, temperature: int) -> None:
        pass

    @abstractmethod
    def cook_pizza(self, pizza: Pizza) -> None:
        pass

    @abstractmethod
    def get_temperature(self) -> int:
        pass

    @abstractmethod
    def get_oven_type(self) -> str:
        pass


class ClassicOvenImplementor(IOvenImplementor):

    def __init__(self, temperature: int = 0):
        self.temperature = temperature
        self.type = "ClassicStove"

    def warm_up(self, temperature: int) -> None:
        # разогрев классической печи
        time.sleep((temperature - self.temperature)/10)
        print(f"Temperature warm up from {self.temperature}"
              f" to {temperature}")
        self.temperature = temperature

    def cool_down(self, temperature: int) -> None:
        # остужаем классическую печь
        time.sleep((self.temperature - temperature)/5)
        print(f"Temperature cool down from {self.temperature}"
              f" to {temperature}")
        self.temperature = temperature

    def cook_pizza(self, pizza: Pizza) -> None:
        time.sleep(pizza.cook_time/10)
        pizza.cook()

    def get_oven_type(self) -> str:
        return self.type

    def get_temperature(self) -> int:
        return self.temperature


class ElectricalOvenImplementor(IOvenImplementor):

    def __init__(self, temperature: int = 0):
        self.temperature = temperature
        self.type = "ElectricalStove"

    def warm_up(self, temperature: int) -> None:
        # разогрев электрической печи
        time.sleep((temperature - self.temperature) / 30)
        print(f"Temperature warm up from {self.temperature}"
              f" to {temperature}")
        self.temperature = temperature

    def cool_down(self, temperature: int) -> None:
        # остужаем электрическую печь
        time.sleep((self.temperature - temperature) / 20)
        print(f"Temperature cool down from {self.temperature}"
              f" to {temperature}")
        self.temperature = temperature

    def cook_pizza(self, pizza: Pizza) -> None:
        time.sleep(pizza.cook_time / 10)
        pizza.cook()

    def get_oven_type(self) -> str:
        return self.type

    def get_temperature(self) -> int:
        return self.temperature


class Oven:

    def __init__(self, implementor: IOvenImplementor):
        self.__implementor = implementor

    def __prepare_stove(self, temperature: int):
        if self.__implementor.get_temperature() > temperature:
            self.__implementor.cool_down(temperature)
        elif self.__implementor.get_temperature() < temperature:
            self.__implementor.warm_up(temperature)
        else:
            print("Ideal temperature")
        print("Oven prepared!")

    def cook_pizza(self, pizza: Pizza) -> None:
        self.__prepare_stove(pizza.cook_temperature)
        print(f"Cooking {pizza.name} pizza for {pizza.cook_time}"
              f" minutes at {pizza.cook_temperature} C")
        self.__implementor.cook_pizza(pizza)
        if pizza.isCooked():
            print("Pizza is ready!!!")
        else:
            print("O_o ... some wrong ...")
        print("---------------------------")

    def change_implementor(self, implementor: IOvenImplementor) -> None:
        self.__implementor = implementor
        print("Implementor changed")

    def get_temperature(self) -> int:
        return self.__implementor.get_temperature()

    def get_implementor_name(self) -> str:
        return self.__implementor.get_oven_type()


if __name__ == "__main__":
    first_pizza = Pizza("Margarita", 10, 220)
    second_pizza = Pizza("Salami", 9, 180)

    implementor = ClassicOvenImplementor()
    oven = Oven(implementor)
    print(f"Implementor type: {oven.get_implementor_name()}")
    oven.cook_pizza(first_pizza)
    oven.cook_pizza(second_pizza)
    # замена реализации
    new_implementor = ElectricalOvenImplementor(oven.get_temperature())
    first_pizza = Pizza("Margarita", 9, 225)
    second_pizza = Pizza("Salami", 10, 175)
    oven.change_implementor(new_implementor)
    print(f"Implementor type: {oven.get_implementor_name()}")
    oven.cook_pizza(first_pizza)
    oven.cook_pizza(second_pizza)