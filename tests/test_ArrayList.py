import random
from typing import Literal
import pytest
from data_structures.ArrayList import ArrayList


class TestArrayList():
    array_list1 = ArrayList(1)
    array_list2 = ArrayList(2)
    
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
        ],
        # ids=[
        #     "length=5 - index=5", 
        #     "length=5 - index=6", 
        #     "length=2 - index=2",
        #     "length=1 - index=1",
        #     "length=0 - index=0"
        # ]
    )
    def test_init(self, array_list_init: list[int] | None | Literal[1], expected_length: Literal[2] | Literal[5] | Literal[7] | Literal[9] | Literal[17] | Literal[1] | Literal[0], expected_capacity: Literal[2] | Literal[5] | Literal[7] | Literal[9] | Literal[17] | Literal[4]):
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
    def test_getitem(self, array_list_init: list[int] | Literal[1], index: Literal[0] | Literal[1] | Literal[3] | Literal[8] | Literal[16] | Literal[-1] | Literal[-2] | Literal[-3] | Literal[-4], expected_value: Literal[0] | Literal[1] | Literal[3] | Literal[8] | Literal[16] | Literal[2]):
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
    def test_getitem_indexError(self, array_list_init: list[int] | None | Literal[1], index: Literal[2] | Literal[-3] | Literal[-18] | Literal[1] | Literal[-2] | Literal[0] | Literal[-1]):
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
    def test_setitem(self, array_list_init: list[int] | Literal[1], index: Literal[0] | Literal[-1] | Literal[1] | Literal[-5], value: Literal[9] | Literal[0] | Literal[8], expected_array_list: list[int] | Literal[8]):
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
    def test_setitem_indexError(self, array_list_init: list[int] | None | Literal[1], index: Literal[5] | Literal[6] | Literal[2] | Literal[1] | Literal[11] | Literal[0] | Literal[10]):
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
    def test_equal(self, array_list_init_1: list[int] | None | Literal[1], array_list_init_2: list[int] | None | Literal[1] | Literal[5], expected_equal: bool):
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
    def test_equal_typeError(self, object_1: ArrayList[int] | ArrayList[None] | list[int], object_2: list[int] | ArrayList[None] | ArrayList[int]):
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
    def test_push(self, array_list_init: None | list[int], items_to_push: list[int], expected_length: Literal[0] | Literal[1] | Literal[4] | Literal[5] | Literal[8] | Literal[9] | Literal[19], expected_capacity: Literal[4] | Literal[8] | Literal[16] | Literal[32]):
        array_list = ArrayList(array_list_init)
        for item in items_to_push:
            array_list.push(item)

        assert array_list.length == expected_length
        assert array_list.capacity == expected_capacity
