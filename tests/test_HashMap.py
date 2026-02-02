import pytest

from src.data_structures.HashMap import HashMap, KeyValuePair


class TestKeyValuePair:
    @pytest.mark.parametrize(
        "key, value, expected_str",
        [
            ("name", "Alice", "'name': 'Alice'"),
            (1, 100, "1: 100"),
            ("age", 25, "'age': 25"),
            (42, "answer", "42: 'answer'"),
        ],
    )
    def test_init_and_str(self, key, value, expected_str):
        kv_pair = KeyValuePair(key, value)
        assert kv_pair.key == key
        assert kv_pair.value == value
        assert str(kv_pair) == expected_str

    @pytest.mark.parametrize(
        "key, value, expected_repr",
        [
            ("name", "Alice", "'name': 'Alice'"),
            (1, 100, "1: 100"),
        ],
    )
    def test_repr(self, key, value, expected_repr):
        kv_pair = KeyValuePair(key, value)
        assert repr(kv_pair) == expected_repr


class TestHashMap:
    def test_init(self):
        hash_map = HashMap()
        assert hash_map.length == 0
        assert hash_map.capacity == 10

    def test_put_single_item(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        assert hash_map.length == 1
        assert hash_map.get("key1") == "value1"

    @pytest.mark.parametrize(
        "items",
        [
            [("a", 1), ("b", 2), ("c", 3)],
            [("x", "apple"), ("y", "banana"), ("z", "cherry")],
            [(1, 100), (2, 200), (3, 300)],
        ],
    )
    def test_put_multiple_items(self, items):
        hash_map = HashMap()
        for key, value in items:
            hash_map.put(key, value)

        assert hash_map.length == len(items)
        for key, value in items:
            assert hash_map.get(key) == value

    def test_put_duplicate_key_raises_error(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        with pytest.raises(KeyError, match="Key: key1 already exists!"):
            hash_map.put("key1", "value2")

    def test_get_existing_key(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        assert hash_map.get("key1") == "value1"

    def test_get_non_existing_key(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        assert hash_map.get("key2") is None

    def test_get_empty_hashmap(self):
        hash_map = HashMap()
        assert hash_map.get("key1") is None

    def test_update_existing_key(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        hash_map.update("key1", "new_value")
        assert hash_map.get("key1") == "new_value"

    def test_update_non_existing_key_raises_error(self):
        hash_map = HashMap()
        with pytest.raises(KeyError, match="Key: key1 does not exist!"):
            hash_map.update("key1", "value")

    def test_remove_existing_key(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        hash_map.put("key2", "value2")

        initial_length = hash_map.length
        assert initial_length == 2
        removed_value = hash_map.remove("key1")
        assert removed_value.value == "value1"
        assert hash_map.length == initial_length - 1
        assert hash_map.get("key1") is None
        assert hash_map.get("key2") == "value2"

    def test_remove_non_existing_key(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        result = hash_map.remove("key2")
        assert result is None

    def test_remove_from_empty_hashmap(self):
        hash_map = HashMap()
        result = hash_map.remove("key1")
        assert result is None

    def test_getitem(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        assert hash_map["key1"] == "value1"

    def test_getitem_non_existing_key(self):
        hash_map = HashMap()
        with pytest.raises(KeyError, match="Key: key1 does not exist!"):
            _ = hash_map["key1"]

    def test_setitem_new_key(self):
        hash_map = HashMap()
        hash_map["key1"] = "value1"
        assert hash_map.get("key1") == "value1"
        assert hash_map.length == 1

    def test_setitem_existing_key(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        hash_map["key1"] = "new_value"
        assert hash_map.get("key1") == "new_value"
        assert hash_map.length == 1

    def test_str_empty(self):
        hash_map = HashMap()
        assert str(hash_map) == "{}"

    def test_str_with_items(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        result = str(hash_map)
        assert "'key1': 'value1'" in result
        assert result.startswith("{")
        assert result.endswith("}")

    def test_repr(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")
        result = repr(hash_map)
        assert "000 ->" in result
        assert "009 ->" in result

    def test_reallocate_container(self):
        hash_map = HashMap()
        # Initial capacity is 10, load factor is 0.7
        # So adding 8 items should trigger reallocation (8/10 > 0.7)
        for i in range(8):
            hash_map.put(f"key{i}", f"value{i}")

        assert hash_map.capacity == 20
        assert hash_map.length == 8

        # Verify all items are still accessible
        for i in range(8):
            assert hash_map.get(f"key{i}") == f"value{i}"

    def test_reallocate_preserves_all_data(self):
        hash_map = HashMap()
        items = [(f"key{i}", f"value{i}") for i in range(15)]

        for key, value in items:
            hash_map[key] = value

        # Should have reallocated at least once
        assert hash_map.capacity > 10
        assert hash_map.length == 15

        # Verify all items
        for key, value in items:
            assert hash_map.get(key) == value

    def test_collision_handling(self):
        # This test verifies that collisions are handled correctly
        # by chaining in the ArrayList buckets
        hash_map = HashMap()

        # Add multiple items
        hash_map.put("a", 1)
        hash_map.put("b", 2)
        hash_map.put("c", 3)

        assert hash_map.get("a") == 1
        assert hash_map.get("b") == 2
        assert hash_map.get("c") == 3

    def test_is_key_in_container(self):
        hash_map = HashMap()
        hash_map.put("key1", "value1")

        assert hash_map._is_key_in_container("key1") is True
        assert hash_map._is_key_in_container("key2") is False

    def test_integer_keys(self):
        hash_map = HashMap()
        hash_map.put(1, "one")
        hash_map.put(2, "two")
        hash_map.put(3, "three")

        assert hash_map.get(1) == "one"
        assert hash_map.get(2) == "two"
        assert hash_map.get(3) == "three"

    def test_mixed_value_types(self):
        hash_map = HashMap()
        hash_map.put("string", "value")
        hash_map.put("int", 42)
        hash_map.put("float", 3.14)
        hash_map.put("list", [1, 2, 3])

        assert hash_map.get("string") == "value"
        assert hash_map.get("int") == 42
        assert hash_map.get("float") == 3.14
        assert hash_map.get("list") == [1, 2, 3]

    def test_update_after_reallocation(self):
        hash_map = HashMap()

        # Add enough items to trigger reallocation
        for i in range(10):
            hash_map.put(f"key{i}", f"value{i}")

        # Update an item that was added before reallocation
        hash_map.update("key0", "new_value0")
        assert hash_map.get("key0") == "new_value0"

    def test_remove_after_reallocation(self):
        hash_map = HashMap()

        # Add enough items to trigger reallocation
        for i in range(10):
            hash_map.put(f"key{i}", f"value{i}")

        # Remove an item that was added before reallocation
        result = hash_map.remove("key0")
        assert result.value == "value0"
        assert hash_map.get("key0") is None

    def test_multiple_operations_sequence(self):
        hash_map = HashMap()

        # Put
        hash_map.put("a", 1)
        hash_map.put("b", 2)
        assert hash_map.length == 2

        # Update
        hash_map.update("a", 10)
        assert hash_map.length == 2  # Length shouldn't change

        # Get
        assert hash_map.get("a") == 10

        # Remove
        hash_map.remove("b")
        assert hash_map.get("b") is None
        assert hash_map.length == 1  # Length should decrease

        # Put again
        hash_map.put("c", 3)
        assert hash_map.get("c") == 3
        assert hash_map.length == 2
