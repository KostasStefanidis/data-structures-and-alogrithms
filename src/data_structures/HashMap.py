from typing import Generic, TypeVar

from ArrayList import ArrayList

K = TypeVar("K")
V = TypeVar("V")
DEFAULT_CAPACITY = 10
DEFAULT_LOAD_FACTOR = 0.7


class KeyValuePair(Generic[K, V]):
    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        if isinstance(self.key, str):
            key_str = f"'{self.key}'"
        else:
            key_str = str(self.key)
        if isinstance(self.value, str):
            value_str = f"'{self.value}'"
        else:
            value_str = str(self.value)
        return f"{key_str}: {value_str}"

    def __repr__(self) -> str:
        return self.__str__()


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

    def __str__(self) -> str:
        output = "{"
        for sub_array in self._data_container:
            for kv_pair in sub_array:
                output += f", {kv_pair}"
        output = output.replace(", ", "", 1)
        output += "}"
        return output

    def __repr__(self) -> str:
        output = ""
        for i in range(self.capacity):
            output += f"{str(i).zfill(3)} -> {self._data_container[i]}\n"
        return output

    def __getitem__(self, key: K):
        if not self._is_key_in_container(key):
            raise KeyError(f"Key: {key} does not exist!")

        return self.get(key)

    def __setitem__(self, key: K, value: V):
        if self._is_key_in_container(key):
            self.update(key, value)
        else:
            self.put(key, value)

    def _is_key_in_container(self, key: K):
        idx = hash(key) % self.capacity
        return any(key == kv_pair.key for kv_pair in self._data_container[idx])

    def put(self, key: K, value: V) -> None:
        if self._is_key_in_container(key):
            raise KeyError(f"Key: {key} already exists!")

        if (self.length + 1) / self.capacity > DEFAULT_LOAD_FACTOR:
            self._reallocate_container()

        idx = hash(key) % self.capacity

        self._data_container[idx].push(KeyValuePair(key, value))
        self.length += 1

    def update(self, key: K, value: V):
        if not self._is_key_in_container(key):
            raise KeyError(f"Key: {key} does not exist!")

        idx = hash(key) % self.capacity
        for kv_pair in self._data_container[idx]:
            if key == kv_pair.key:
                kv_pair.value = value

    def get(self, key: K):
        idx = hash(key) % self.capacity
        for kv_pair in self._data_container[idx]:
            if key == kv_pair.key:
                return kv_pair.value

        return None

    def remove(self, key: K):
        idx = hash(key) % self.capacity
        sub_array = self._data_container[idx]

        for idx, kv_pair in enumerate(sub_array):
            if key == kv_pair.key:
                return sub_array.remove(idx)

        return None

    def _reallocate_container(self):
        print(f"Load factor {DEFAULT_LOAD_FACTOR} reached. Reallocating data container.")
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
