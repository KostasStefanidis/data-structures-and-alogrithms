import random
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
    def test_init(self, array_list_init, expected_length, expected_capacity):
        array_list = ArrayList(array_list_init)
        assert array_list.length == expected_length
        assert array_list.capacity == expected_capacity
    
    
    def test_getitem_indexError(self):
        index = self.array_list1.length + random.randint(1,10)
        with pytest.raises(IndexError):
            _ = self.array_list1[index]

        # _ = self.array_list1[0]
    
    
    @pytest.mark.parametrize(
        "array_list_init, index",
        [
            ([1,2,3,4,5], 5),
            ([1,2,3,4,5], 6),
            ([1,2], 2),
            (1, 1),
            (None, 0)
        ],
        ids=[
            "length=5 - index=5", 
            "length=5 - index=6", 
            "length=2 - index=2",
            "length=1 - index=1",
            "length=0 - index=0"
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
