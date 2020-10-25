from abc import ABC, abstractmethod


class IOven(ABC):
    """Исходный интерфейс плиты,
    где единица измерения температуры - F"""
    @abstractmethod
    def get_temperature(self) -> float:
        pass

    @abstractmethod
    def set_temperature(self, t: float) -> None:
        pass


class ICelsiusOven(ABC):
    """Интерфейс плиты с которым будем осуществлять
    работу в рамках разрабатываемой системы,
    где единица измерения температуры - C"""
    @abstractmethod
    def get_celsius_temperature(self) -> float:
        pass

    @abstractmethod
    def set_celsius_temperature(self, t: float) -> None:
        pass

    @abstractmethod
    def get_original_temperature(self) -> float:
        pass


class OriginalOven(IOven):
    """Класс кухонной плиты, который будем адаптировать"""
    def __init__(self, t: float):
        assert t >= 32, "Мы тут не холодильник реализуем"
        self.temperature = t

    def set_temperature(self, t: float) -> None:
        assert t >= 32, "Печь которая может морозить? Хм... " \
                        "интересненько"
        self.temperature = t

    def get_temperature(self) -> float:
        return self.temperature


class OvenAdapter(ICelsiusOven):
    """Адаптер, позволяющий работать с плитой, где
     единица измерения температуры фаренгейты в
     градусах цельсия"""
    CELSIUS_TO_FAHRENHEIT: float = 9.0/5.0
    FAHRENHEIT_TO_CELSIUS: float = 5.0/9.0
    FAHRENHEIT_ZERO: float = 32.0

    def __init__(self, original_stove: IOven):
        self.stove = original_stove
        self.temperature = self._init_temperature()

    def get_original_temperature(self) -> float:
        return self.stove.get_temperature()

    def _init_temperature(self) -> float:
        return (OvenAdapter.FAHRENHEIT_TO_CELSIUS *
                (self.stove.get_temperature() -
                 OvenAdapter.FAHRENHEIT_ZERO))

    def get_celsius_temperature(self) -> float:
        return self.temperature

    def set_celsius_temperature(self, t: float) -> None:

        new_temperature_stove = (OvenAdapter.CELSIUS_TO_FAHRENHEIT * t +
                                 OvenAdapter.FAHRENHEIT_ZERO)
        self.stove.set_temperature(new_temperature_stove)
        self.temperature = t

if __name__ == "__main__":
    def print_temperature(stove: ICelsiusOven):
        print(f"Original temperature = {stove.get_original_temperature()}"
              f" F")
        print(f"Celsius temperature = {stove.get_celsius_temperature()}")

    fahrenheit_stove = OriginalOven(32)
    celsius_stove = OvenAdapter(fahrenheit_stove)
    print_temperature(celsius_stove)
    celsius_stove.set_celsius_temperature(180)
    print("----------------")
    print("New temperature")
    print("----------------")
    print_temperature(celsius_stove)


