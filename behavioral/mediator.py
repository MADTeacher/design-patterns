from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from random import choice


class OrderType(Enum):
    """Типы возможных заказов"""
    FOOD = 1
    BINGE = 2


class Order:
    """Класс заказа"""
    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"заказ под #{self.id} ({self.type.name})"


class Event(Enum):
    """Типы событий обработки заказов"""
    GET_ORDER = 1
    FINISH_ORDER = 2


class WorkerType(Enum):
    """Типы работников пиццерии"""
    WAITER = 1
    CHIEF = 2
    BARMAN = 3


class IMediator(ABC):
    """Интерфейс посредника"""

    @abstractmethod
    def notify(self, worker: Worker, order: Order, event: Event):
        ...

    @abstractmethod
    def add_worker(self, worker: Worker) -> None:
        ...


class Worker(ABC):
    """Абстрактный базовый класс для
    всех сотрудников пиццерии"""

    def __init__(self, name: str, mediator: IMediator):
        self.mediator = mediator
        self.name = name
        self.orders = []
        mediator.add_worker(self)

    @abstractmethod
    def take_order(self, order: Order):
        ...

    @abstractmethod
    def finish_order(self, order: Order):
        ...

    @abstractmethod
    def type(self) -> WorkerType:
        ...

    def get_orders_id(self) -> List[int]:
        return [it.id for it in self.orders]


class Waiter(Worker):
    """Класс официанта"""

    def __init__(self, name: str, mediator: IMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Официант {self.name} принял {order}")
        self.mediator.notify(self, order, Event.GET_ORDER)

    def finish_order(self, order: Order):
        print(f"Официант {self.name} отнес {order} клиенту")
        self.orders.remove(order)

    def type(self) -> WorkerType:
        return WorkerType.WAITER


class Barman(Worker):
    """Класс бармена"""

    def __init__(self, name: str, mediator: IMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Бармен {self.name} принял {order}")

    def finish_order(self, order: Order):
        print(f"Бармен {self.name} выполнил ")
        self.mediator.notify(self, order, Event.FINISH_ORDER)

    def processing_order(self):
        if self.orders:
            order = self.orders.pop()
            print(f"Бармен {self.name} выполняет {order}")
            self.finish_order(order)
        else:
            print(f"Бармен {self.name} грустно разводит руками")

    def type(self) -> WorkerType:
        return WorkerType.BARMAN


class Chief(Worker):
    """Класс шеф-повара"""

    def __init__(self, name: str, mediator: IMediator):
        super().__init__(name, mediator)

    def take_order(self, order: Order):
        self.orders.append(order)
        print(f"Шеф {self.name} принял {order}")

    def finish_order(self, order: Order):
        print(f"Шеф {self.name} выполнил {order}")
        self.mediator.notify(self, order, Event.FINISH_ORDER)

    def processing_order(self):
        if self.orders:
            order = self.orders.pop()
            print(f"Шеф {self.name} выполняет {order}")
            self.finish_order(order)
        else:
            print(f"Шеф {self.name} от нечего делать шинкует капусту")

    def type(self) -> WorkerType:
        return WorkerType.CHIEF


class WorkersMediator(IMediator):
    """Посредник обмена сообщениями между
    работниками пиццерии"""

    def __init__(self):
        self.workers = {WorkerType.WAITER: [],
                        WorkerType.BARMAN: [],
                        WorkerType.CHIEF: []}

    def add_worker(self, worker: Worker):
        if worker not in self.workers[worker.type()]:
            self.workers[worker.type()].append(worker)

    def remove_worker(self, worker: Worker):
        if worker in self.workers[worker.type()]:
            self.workers[worker.type()].remove(worker)
        if len(self.workers[worker.type()]) == 0:
            print(f"Внимание работники типа {worker.type().name} "
                  f" отсутствуют!!!")

    def notify(self, worker: Worker, order: Order, event: Event):
        if (event is Event.GET_ORDER and
                worker.type() is WorkerType.WAITER):
            if order.type is OrderType.FOOD:
                chef: Chief = choice(self.workers[WorkerType.CHIEF])
                chef.take_order(order)
            else:
                barman: Barman = choice(self.workers[WorkerType.BARMAN])
                barman.take_order(order)
        elif (event is Event.FINISH_ORDER and
              (worker.type() is WorkerType.BARMAN or
               worker.type() is WorkerType.CHIEF)):
            for waiter in self.workers[WorkerType.WAITER]:
                if order.id in waiter.get_orders_id():
                    waiter.finish_order(order)
                    break
            else:
                print(f"{order} не был доставлен клиенту!!!")
        else:
            raise NotImplemented("Это что ещё за зверь? Оо")


if __name__ == "__main__":
    mediator = WorkersMediator()
    waiter1 = Waiter("Александр", mediator)
    waiter2 = Waiter("Георгий", mediator)
    waiter3 = Waiter("Максим", mediator)
    barmen1 = Barman("Герман", mediator)
    barmen2 = Barman("Алексей", mediator)
    chief = Chief("Станислав", mediator)

    orders = [Order(choice([OrderType.FOOD, OrderType.BINGE]))
              for _ in range(10)]
    for it in orders:
        print("*"*30)
        choice([waiter1, waiter2, waiter3]).take_order(it)
    print("*" * 39)
    print("*"*8 + "Шеф-повар готовит блюда"+8*"*")
    print("*" * 39)
    for it in range(6):
        chief.processing_order()
        print("*" * 30)
    print("*" * 42)
    print("*"*8 + "Бармены смешивают коктейли"+8*"*")
    print("*" * 42)
    for it in range(7):
        choice([barmen1, barmen2]).processing_order()
        print("*" * 30)


