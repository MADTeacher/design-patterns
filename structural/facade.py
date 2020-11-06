from abc import ABC, abstractmethod
from enum import Enum

###################Menu and IClient########################
class MenuType(Enum):
    """Тип меню"""
    VEGAN = 1
    NOT_VEGAN = 2
    MIXED = 3


class IMenu(ABC):
    """
    Базовый класс, задающий
    интерфейс создаваемых меню
    """
    @abstractmethod
    def get_name(self):
        pass


class VeganMenu(IMenu):
    def get_name(self):
        return "Вегетарианское меню"


class NotVeganMenu(IMenu):
    def get_name(self):
        return "Не вегетарианское меню"


class MixedMenu(IMenu):
    def get_name(self):
        return "Смешанное меню"


class IClient(ABC):
    """
    Базовый класс, задающий
    интерфейс клиентов пиццерии
    """
    @abstractmethod
    def request_menu(self, menu: IMenu):
        ...

    @abstractmethod
    def form_order(self) -> dict:
        ...

    @abstractmethod
    def eating_food(self):
        ...

    @abstractmethod
    def get_name(self):
        ...


#####################################################


class Kitchen:
    """
    Кухня
    """
    def prepare_food(self):
        print("Заказанная еда готовится!")

    def call_waiter(self):
        print("Отдаем приготовленную еду официанту")


class Waiter:
    """
    Официант
    """
    def take_order(self, client: IClient):
        print(f"Официант принял заказ клиента {client.get_name()}")

    def send_to_kitchen(self, kitchen: Kitchen):
        print("Официант отнес заказ на кухню")

    def serve_client(self, client: IClient):
        print(f"Блюда готовы, несем клиенту c именем {client.get_name()}!")


class PizzeriaFacade:
    """
    Пиццерия на основе паттерна 'Фасад'
    """
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        self.menu = {MenuType.VEGAN: VeganMenu,
                     MenuType.NOT_VEGAN: NotVeganMenu,
                     MenuType.MIXED: MixedMenu}

    def get_menu(self, type_menu: MenuType) -> IMenu:
        return self.menu[type_menu]()

    def take_order(self, client: IClient):
        self.waiter.take_order(client)
        self.waiter.send_to_kitchen(self.kitchen)
        self.__kitchen_work()
        self.waiter.serve_client(client)

    def __kitchen_work(self):
        self.kitchen.prepare_food()
        self.kitchen.call_waiter()


class Client(IClient):
    """
    Класс клиента пиццерии
    """
    def __init__(self, name: str):
        self.name = name

    def request_menu(self, menu: IMenu):
        print(f"Клиент {self.name} ознакамливается с '{menu.get_name()}'")

    def form_order(self) -> dict:
        print(f"Клиент {self.name} делает заказ")
        return {}

    def eating_food(self):
        print(f"Клиент {self.name} приступает к трапезе")

    def get_name(self):
        return self.name


if __name__ == "__main__":
    pizzeria = PizzeriaFacade()
    client1 = Client("Иван")
    client2 = Client("Александр")
    client1.request_menu(pizzeria.get_menu(MenuType.MIXED))
    pizzeria.take_order(client1)
    client2.request_menu(pizzeria.get_menu(MenuType.VEGAN))
    pizzeria.take_order(client2)
    client1.eating_food()
    client2.eating_food()

