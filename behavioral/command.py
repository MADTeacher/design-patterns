from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    """Интерфейсный класс для выполняемых операций"""
    @abstractmethod
    def execute(self) -> None:
        ...


class ChiefAssistant:
    def prepare_pizza_dough(self):
        print("Ассистент подготавливает тесто для пиццы")

    def prepare_topping(self):
        print("Ассистент нарезает начинку для пиццы")

    def prepare_sauce(self):
        print("Ассистент готовит соус")


class Stove:
    def prepare_stove(self):
        print("Печь разогревается")

    def cooking_pizza(self):
        print("Пицца готовится в печи")


class ChiefCooker:
    def make_pizza_base(self):
        print("Шеф раскатывает основу для пиццы")

    def applied_sauce(self):
        print("Шеф наносит соус на основу пиццы")

    def add_topping_to_pizza(self):
        print("Шеф добавляет начинку на пиццу")

    def bon_appetit(self):
        print("Шеф желает клиенту приятного аппетита!")


class PrepareStoveCommand(ICommand):
    """Класс команды для разогрева печи"""
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_stove()


class PrepareDoughCommand(ICommand):
    """Класс команды для подготовки теста пиццы"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_pizza_dough()


class PrepareToppingCommand(ICommand):
    """Класс команды для нарезки начинки пиццы"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_topping()


class PrepareSauceCommand(ICommand):
    """Класс команды для приготовления соуса"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_sauce()


class CookingPizzaCommand(ICommand):
    """Класс команды для приготовления пиццы в печи"""
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cooking_pizza()


class MakePizzaBaseCommand(ICommand):
    """Класс команды для приготовления основы для пиццы"""
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.make_pizza_base()


class AppliedSauceCommand(ICommand):
    """Класс команды для нанесения соуса на пиццу"""
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.applied_sauce()


class AddToppingCommand(ICommand):
    """Класс команды для добавления начинки на пиццу"""

    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_topping_to_pizza()


class BonAppetitCommand(ICommand):
    """Класс команды для пожелания клиенту
       приятного аппетита"""

    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.bon_appetit()


class Pizzeria:
    """Класс агрегации всех команд для приготовления
       пиццы"""
    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print("Не задана очередность выполнения"
                  " команд приготовления пиццы")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    chief = ChiefCooker()
    assistant = ChiefAssistant()
    stove = Stove()
    pizzeria = Pizzeria()
    # формируем последовательность команд для приготовления пиццы
    pizzeria.addCommand(PrepareDoughCommand(assistant))
    pizzeria.addCommand(MakePizzaBaseCommand(chief))
    pizzeria.addCommand(PrepareSauceCommand(assistant))
    pizzeria.addCommand(AppliedSauceCommand(chief))
    pizzeria.addCommand(PrepareStoveCommand(stove))
    pizzeria.addCommand(PrepareToppingCommand(assistant))
    pizzeria.addCommand(AddToppingCommand(chief))
    pizzeria.addCommand(CookingPizzaCommand(stove))
    pizzeria.addCommand(BonAppetitCommand(chief))
    # запускаем процесс приготовления пиццы
    pizzeria.cook()
