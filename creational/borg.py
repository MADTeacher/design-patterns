class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class MonostateSingleton(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.name = "MySingleton"

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

class NewSingleton(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.name = "MySingleton"

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

if __name__ == "__main__":
    my_singleton1 = MonostateSingleton()
    print("Singleton1 name: " + my_singleton1.get_name())
    my_singleton2 = MonostateSingleton()
    my_singleton2.set_name("New Singleton")
    print("Singleton2 name: " + my_singleton2.get_name())
    print("Singleton2 name: " + my_singleton1.name)
    print(my_singleton1)
    print(my_singleton2)
    print(id(my_singleton1) == id(my_singleton2))