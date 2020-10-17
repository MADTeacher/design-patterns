class Platter:

    def __init__(self, platter_id: int):
        self._empty = True
        self._platter_id = platter_id

    @property
    def get_id(self):
        return self._platter_id

    def is_empty(self):
        return not self._empty

    def set_pizza(self):
        self._empty = False

    def get_pizza(self):
        self.reset()

    def reset(self):
        self._empty = True

    def __str__(self):
        return f"Platter id: {self._platter_id}, empty: {self._empty}"


class ObjectPool:
    def __init__(self, size: int):
        self.__pool_size = size
        self.__resources = [Platter(it) for it in range(size)]

    def getObject(self) -> Platter:
        if len(self.__resources) > 0:
            return self.__resources.pop(0)
        else:
            raise IndexError("Object pool is empty")

    def releaseObject(self, release_object: Platter):
        release_object.reset()
        self.__resources.append(release_object)

    def free_objects_amount(self):
        return len(self.__resources)

    def __str__(self):
        return f"Amount objects into pool: {len(self.__resources)}"


if __name__ == "__main__":
    obj_pool = ObjectPool(3)
    print(obj_pool)
    my_platter = obj_pool.getObject()
    print(my_platter)
    print(obj_pool)
    my_platter.set_pizza()
    print(my_platter)
    obj_pool.releaseObject(my_platter)
    print(obj_pool)
    [obj_pool.getObject() for _ in range(4)]

