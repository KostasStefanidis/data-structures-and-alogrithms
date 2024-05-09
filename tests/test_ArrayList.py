import pytest
from src.data_structures.ArrayList import ArrayList

class TestArrayList():    
    @pytest.mark.parametrize(
        "array_list_init, expected_length, expected_capacity",
        [   
            (list(range(2)), 2, 2),
            (list(range(5)), 5, 5),
            (list(range(7)), 7, 7),
            (list(range(9)), 9, 9),
            (list(range(17)), 17, 17),
            (1, 1, 4),
            (None, 0, 4),
        ]
    )
    def test_init(self, array_list_init, expected_length, expected_capacity):
        array_list = ArrayList(array_list_init)
        assert array_list.length == expected_length
        assert array_list.capacity == expected_capacity
    
    
    @pytest.mark.parametrize(
        "array_list_init, index, expected_value",
        [   
            (list(range(2)), 0, 0),
            (list(range(5)), 1, 1),
            (list(range(7)), 3, 3),
            (list(range(9)), 8, 8),
            (list(range(17)), 16, 16),
            (1, 0, 1),
            (list(range(4)), -1, 3),
            (list(range(4)), -2, 2),
            (list(range(4)), -3, 1),
            (list(range(4)), -4, 0)
        ],
    )
    def test_getitem(self, array_list_init, index, expected_value):
        array_list = ArrayList(array_list_init)
        assert array_list[index] == expected_value
    
    
    @pytest.mark.parametrize(
        "array_list_init, index",
        [   
            (list(range(2)), 2),
            (list(range(2)), -3),
            (list(range(17)), -18),
            (1, 1),
            (1, -2),
            (None, 0),
            (None, -1)
        ],
    )
    def test_getitem_indexError(self, array_list_init, index):
        array_list = ArrayList(array_list_init)
        with pytest.raises(IndexError):
            _ = array_list[index]
    
    
    @pytest.mark.parametrize(
        "array_list_init, index, value, expected_array_list",
        [
            ([1,2,3,4,5], 0, 9, [9,2,3,4,5]),
            ([1,2,3,4,5], -1, 9, [1,2,3,4,9]),
            ([5,10,15], 1, 0, [5,0,15]),
            (1, 0, 8, 8),
            ([1,2,3,4,5], -5, 9, [9,2,3,4,5]),
        ]
    )
    def test_setitem(self, array_list_init, index, value, expected_array_list):
        array_list = ArrayList(array_list_init)
        array_list[index] = value
        assert array_list == ArrayList(expected_array_list)
    
    @pytest.mark.parametrize(
        "array_list_init, index",
        [
            ([1,2,3,4,5], 5),
            ([1,2,3,4,5], 6),
            ([1,2], 2),
            (1, 1),
            (1, 11),
            (None, 0),
            (None, 10)
        ]
    )
    def test_setitem_indexError(self, array_list_init, index):
        array_list = ArrayList(array_list_init)
        with pytest.raises(IndexError):
            array_list[index] = 0

    
    @pytest.mark.parametrize(
        "array_list_init_1, array_list_init_2, expected_equal",
        [
            (list(range(5)), list(range(5)), True),
            (list(range(5)), list(range(22)), False),
            ([1,2], [1,3], False),
            ([5,6,11], [83,50,18], False),
            ([5,6,11], [11,6,5], False),
            (1, 1, True),
            (1, 5, False),
            (None, None, True)
        ]
    )
    def test_equal(self, array_list_init_1, array_list_init_2, expected_equal):
        array_list_1 = ArrayList(array_list_init_1)
        array_list_2 = ArrayList(array_list_init_2)
        assert (array_list_1 == array_list_2) == expected_equal


    @pytest.mark.parametrize(
        "object_1, object_2",
        [
            (ArrayList(list(range(5))), list(range(5))),
            (ArrayList(list(range(5))), list(range(22))),
            (ArrayList(1), [1,3]),
            (ArrayList(), [1,3]),
            (list(range(100)), ArrayList()),
            ([0,8,14,9], ArrayList([1,3])),
        ]
    )
    def test_equal_typeError(self, object_1, object_2):
        with pytest.raises(TypeError):
            object_1 == object_2
    
    
    # def test_iterator():
        
    
    @pytest.mark.parametrize(
        "array_list_init, items_to_push, expected_length, expected_capacity",
        [
            (None, [], 0, 4),
            (None, [1], 1, 4),
            (None, list(range(4)), 4, 4),
            (None, list(range(5)), 5, 8),
            (None, list(range(8)), 8, 8),
            (None, list(range(9)), 9, 16),
            (list(range(2)), list(range(2)), 4, 4),
            (list(range(2)), list(range(17)), 19, 32),
        ]
    )
    def test_push(self, array_list_init, items_to_push, expected_length, expected_capacity):
        array_list = ArrayList(array_list_init)
        for item in items_to_push:
            array_list.push(item)

        assert array_list.length == expected_length
        assert array_list.capacity == expected_capacity


    @pytest.mark.parametrize(
        "array_list_init, index, expected_array, expected_returned_item",
        [
            ([0,1,2,3,4], None, [0,1,2,3], 4),
            ([0,1,2,3,4], 0, [1,2,3,4], 0),
            ([0,1,2,3,4], 2, [0,1,3,4], 2),
            (list(range(10)), None, list(range(9)), 9),
        ]
    )
    def test_remove(self, array_list_init, index, expected_array, expected_returned_item):
        array_list = ArrayList(array_list_init)
        item = array_list.remove(index)
        assert item == expected_returned_item
        assert array_list.get_array() == expected_array


    @pytest.mark.parametrize(
        "array_list_init, index",
        [
            (None, None),
            (None, 0),
            (None, 6),
            ([0,1,2,3,4,5], 6),
            ([1,2,3], 3)
        ]
    )
    def test_remove_index_error(self, array_list_init, index):
        array_list = ArrayList(array_list_init)
        with pytest.raises(IndexError):
            _ = array_list.remove(index)


    @pytest.mark.parametrize(
        "array_list_init, expected_array, expected_returned_item",
        [
            (list(range(3)), list(range(2)), 2),
            (list(range(5)), list(range(4)), 4),
            (list(range(7)), list(range(6)), 6),
            (5, [], 5),
        ]
    )
    def test_pop(self, array_list_init, expected_array, expected_returned_item):
        array_list = ArrayList(array_list_init)
        item = array_list.pop()
        assert item == expected_returned_item
        assert array_list.get_array() == expected_array

    
    @pytest.mark.parametrize(
        "array_list_init, expected_array, expected_returned_item",
        [
            (list(range(0, 3)), list(range(1, 3)), 0),
            (list(range(9, 20)), list(range(10, 20)), 9),
            (5, [], 5)
        ]
    )
    def test_deque(self, array_list_init, expected_array, expected_returned_item):
        array_list = ArrayList(array_list_init)
        item = array_list.deque()
        assert item == expected_returned_item
        assert array_list.get_array() == expected_array
