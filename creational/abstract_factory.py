from abc import ABC, abstractmethod

"""
Базовые классы графического пользовательского интерфейса
"""


class StatusBar(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self): pass


class MainMenu(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self): pass


class MainWindow(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self): pass


"""
Производные классы графического пользовательского интерфейса
для операционной системы Windows
"""


class WindowsStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created status bar for {self._system}')


class WindowsMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created main menu for {self._system}')


class WindowsMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f'Created MainWindow for {self._system}')


"""
Производные классы графического пользовательского интерфейса
для операционной системы Linux
"""


class LinuxStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created status bar for {self._system}')


class LinuxMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created main menu for {self._system}')


class LinuxMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f'Created MainWindow for {self._system}')


"""
Базовый класс абстрактной фабрики
"""


class GuiAbstractFactory(ABC):
    @abstractmethod
    def getStatusBar(self) -> StatusBar: pass

    @abstractmethod
    def getMainMenu(self) -> MainMenu: pass

    @abstractmethod
    def getMainWindow(self) -> MainWindow: pass


"""
Производные классы абстрактной фабрики,
конкретные реализации для каждой из операционных систем
"""


class WindowsGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return WindowsStatusBar()

    def getMainMenu(self) -> MainMenu:
        return WindowsMainMenu()

    def getMainWindow(self) -> MainWindow:
        return WindowsMainWindow()


class LinuxGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return LinuxStatusBar()

    def getMainMenu(self) -> MainMenu:
        return LinuxMainMenu()

    def getMainWindow(self) -> MainWindow:
        return LinuxMainWindow()


"""
Клиентский класс, использующий фабрику для создания GUI
"""


class Application:
    def __init__(self, factory: GuiAbstractFactory):
        self._gui_factory = factory

    def create_gui(self):
        mainwindow = self._gui_factory.getMainWindow()
        status_bar = self._gui_factory.getStatusBar()
        main_menu = self._gui_factory.getMainMenu()
        mainwindow.create()
        main_menu.create()
        status_bar.create()


def create_factory(system_name: str) -> GuiAbstractFactory:
    factory_dict = {
        "Windows": WindowsGuiFactory,
        "Linux": LinuxGuiFactory
    }
    return factory_dict[system_name]()

if __name__ == '__main__':
    system_name = "Linux"
    ui = create_factory(system_name)
    app = Application(ui)
    app.create_gui()
