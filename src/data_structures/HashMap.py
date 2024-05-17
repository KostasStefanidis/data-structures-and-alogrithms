from typing import Generic, TypeVar

from .ArrayList import ArrayList

K = TypeVar("K")
V = TypeVar("V")
DEFAULT_CAPACITY = 10
DEFAULT_LOAD_FACTOR = 0.7


class KeyValuePair(Generic[K, V]):
    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value


class HashMap(Generic[K, V]):
    capacity: int
    length: int
    _data_container: ArrayList[ArrayList[KeyValuePair[K, V]]]

    def __init__(self) -> None:
        self.capacity = DEFAULT_CAPACITY
        self.length = 0

        self._data_container = ArrayList()
        for _ in range(self.capacity):
            self._data_container.push(ArrayList())
        print(self._data_container)

    def __str__(self) -> str:
        return str(self._data_container)

    # def __repr__(self) -> str:

    def __getitem__(self, key: K):
        if not self._is_key_in_container(key):
            raise ValueError(f"Key: {key} does not exist!")

        return self.get(key)

    def __setitem__(self, key: K, value: V):
        if not self._is_key_in_container(key):
            self.put(key, value)
        else:
            self.update(key, value)

    def _is_key_in_container(self, key: K):
        idx = hash(key) % self.capacity
        return any(key == kv_pair.key for kv_pair in self._data_container[idx])
        # for kv_pair in self._data_container[idx]:
        #     if key == kv_pair.key:
        #         return True
        # return False

    def put(self, key: K, value: V) -> None:
        if (self.length + 1) / self.capacity > DEFAULT_LOAD_FACTOR:
            self._reallocate_container()

        idx = hash(key) % self.capacity
        print(idx)

        self._data_container[idx].push(KeyValuePair(key, value))
        self.length += 1

    def update(self, key: K, value: V):
        if not self._is_key_in_container(key):
            raise ValueError(f"Key: {key} does not exist!")

        self._data_container[hash(key) % self.capacity] = KeyValuePair(key, value)

    def get(self, key: K):
        idx = hash(key) % self.capacity
        for kv_pair in self._data_container[idx]:
            if key == kv_pair.key:
                return kv_pair.value

        return None

    def remove(self, key: K):
        idx = hash(key) % self.capacity
        sub_array = self._data_container[idx]
        for i in len(sub_array):
            if key == sub_array[i].key:
                kv_pair = sub_array.remove(i)

        return kv_pair.value

    def _reallocate_container(self):
        self.capacity = self.capacity * 2

        new_data_container: ArrayList[ArrayList[KeyValuePair]] = ArrayList()
        for _ in range(self.capacity):
            new_data_container.push(ArrayList())

        # rehash keys and add them to the new container
        for item in self._data_container:
            if len(item) == 0:
                continue

            for kv_pair in item:
                idx = hash(kv_pair.key) % self.capacity
                new_data_container[idx].push(KeyValuePair(kv_pair.key, kv_pair.value))

        self._data_container = new_data_container


# foo = HashMap()
