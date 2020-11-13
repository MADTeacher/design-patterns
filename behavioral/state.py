from typing import Dict
from abc import ABC, abstractmethod
from enum import Enum


class CoffeeState(Enum):
    """Возможные состояния кофе-машины"""
    IDLE = 0
    CHOOSE = 1
    CAPPUCCINO = 2
    LATTE = 3
    ESPRESSO = 4
    CHANGE_MONEY = 5


class State(ABC):
    """Базовый класс состояния,
    определяющий интерфейс"""

    @abstractmethod
    def insert_money(self, coffee_machine) -> None:
        ...

    @abstractmethod
    def eject_money(self, coffee_machine) -> None:
        ...

    @abstractmethod
    def make_coffee(self, coffee_machine) -> None:
        ...


class IdleState(State):
    """Состояние ожидания"""
    def insert_money(self, coffee_machine) -> None:
        print("Переходим к состоянию выбора коффе")
        coffee_machine.set_state(CoffeeState.CHOOSE)

    def eject_money(self, coffee_machine) -> None:
        print("Какие такие деньги? оО")

    def make_coffee(self, coffee_machine) -> None:
        print("Говорят на халяву и уксус сладок...")


class WaitChooseState(State):
    """Состояние выбора приготовляемого коффе"""
    def insert_money(self, coffee_machine) -> None:
        print("Загружено достаточно средств для заказа?")

    def eject_money(self, coffee_machine) -> None:
        print("Заказывай или оставь свои деньги!")

    def make_coffee(self, coffee_machine) -> None:
        if coffee_machine.next_state is None:
            print("Выберете какой кофе хотите приготовить!")
        else:
            coffee_machine.set_state(coffee_machine.next_state)


class ChangeState(State):
    """Состояние выбора приготовляемого коффе"""
    def insert_money(self, coffee_machine) -> None:
        self.eject_money(coffee_machine)

    def eject_money(self, coffee_machine) -> None:
        print(f"Возврат {coffee_machine.money} рублей")
        coffee_machine.money = 0
        coffee_machine.set_state(CoffeeState.IDLE)

    def make_coffee(self, coffee_machine) -> None:
        self.eject_money(coffee_machine)


class CappuccinoState(State):
    """Состояние приготовления купучино"""

    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def eject_money(self, coffee_machine) -> None:
        print("Не дождешься!!!")

    def make_coffee(self, coffee_machine) -> None:
        cost = 32
        water = 0.3
        milk = 0.1
        if coffee_machine.money >= cost:
            if (coffee_machine.water >= water and
                    coffee_machine.milk >= milk):
                print("Готовим Капучино!")
                coffee_machine.water -= water
                coffee_machine.milk -= milk
                coffee_machine.money -= cost
            else:
                print("Не хватает ингридиентов!")
            if coffee_machine.money > 0:
                coffee_machine.set_state(CoffeeState.CHANGE_MONEY)
                coffee_machine.return_money()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print("Недостаточно средств для приготовления!")


class LatteState(State):
    """Состояние приготовления латте"""

    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def eject_money(self, coffee_machine) -> None:
        print("Не дождешься!!!")

    def make_coffee(self, coffee_machine) -> None:
        cost = 40
        water = 0.3
        milk = 0.2
        if coffee_machine.money >= cost:
            if (coffee_machine.water >= water and
                    coffee_machine.milk >= milk):
                print("Готовим Латте!")
                coffee_machine.water -= water
                coffee_machine.milk -= milk
                coffee_machine.money -= cost
            else:
                print("Не хватает ингридиентов!")
            if coffee_machine.money > 0:
                coffee_machine.set_state(CoffeeState.CHANGE_MONEY)
                coffee_machine.return_money()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print("Недостаточно средств для приготовления!")


class EspressoState(State):
    """Состояние приготовления espresso'"""

    def insert_money(self, coffee_machine) -> None:
        self.make_coffee(coffee_machine)

    def eject_money(self, coffee_machine) -> None:
        print("Не дождешься!!!")

    def make_coffee(self, coffee_machine) -> None:
        cost = 25
        water = 0.3
        if coffee_machine.money >= cost:
            if coffee_machine.water >= water:
                print("Готовим espresso!")
                coffee_machine.water -= water
                coffee_machine.money -= cost
            else:
                print("Не хватает ингридиентов!")
            if coffee_machine.money > 0:
                coffee_machine.set_state(CoffeeState.CHANGE_MONEY)
                coffee_machine.return_money()
            else:
                coffee_machine.set_state(CoffeeState.IDLE)
        else:
            print("Недостаточно средств для приготовления!")


class CoffeeMachine:
    """Класс кофе-машины"""
    def __init__(self, water: float,
                 milk: float, money: int):
        self.water = water
        self.milk = milk
        self.money = money
        self.money: int = 0
        self.eject_money: int = 0
        self.__states: Dict[CoffeeState, State] = {
            CoffeeState.IDLE: IdleState(),
            CoffeeState.CHOOSE: WaitChooseState(),
            CoffeeState.CAPPUCCINO: CappuccinoState(),
            CoffeeState.LATTE: LatteState(),
            CoffeeState.ESPRESSO: EspressoState(),
            CoffeeState.CHANGE_MONEY: ChangeState(),
        }
        self.__state: State = self.__states[CoffeeState.IDLE]
        self.next_state: CoffeeState = None

    def get_state(self, state: CoffeeState):
        return self.__states[state]

    def set_state(self, state: CoffeeState):
        self.__state = self.__states[state]

    def insert_money(self, money: int) -> None:
        self.money += money
        print(f"Внесено {self.money} рублей")
        self.__state.insert_money(self)


    def cappuccino(self) -> None:
        print(f"Выбран режим приготовления Капучино")
        self.next_state = CoffeeState.CAPPUCCINO
        self.__state.make_coffee(self)

    def espresso(self) -> None:
        print(f"Выбран режим приготовления Espresso")
        self.next_state = CoffeeState.ESPRESSO
        self.__state.make_coffee(self)

    def latte(self) -> None:
        print(f"Выбран режим приготовления Латте")
        self.next_state = CoffeeState.LATTE
        self.__state.make_coffee(self)

    def make_coffee(self):
        print("Запуск приготовления выбранного кофе!")
        self.__state.make_coffee(self)

    def return_money(self):
        self.__state.eject_money(self)


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(1.0, 1.0, 1000)
    coffee_machine.make_coffee()
    coffee_machine.insert_money(10)
    coffee_machine.insert_money(10)
    coffee_machine.cappuccino()
    coffee_machine.make_coffee()
    coffee_machine.insert_money(20)
    print("**** Когда мало продуктов для приготовления кофе ****")
    coffee_machine = CoffeeMachine(0.1, 0.1, 1000)
    coffee_machine.insert_money(100)
    coffee_machine.make_coffee()
    coffee_machine.latte()
    coffee_machine.make_coffee()
