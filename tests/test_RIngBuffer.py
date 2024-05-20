import pytest

from src.data_structures.RingBuffer import RingBuffer


class TestRingBuffer:
    @pytest.mark.parametrize(
        "buffer_init, expected_head, expected_tail",
        [
            (list(range(2)), 0, 1),
            (list(range(5)), 0, 4),
            (1, 0, 0),
            (None, 0, 3),
        ],
    )
    def test_init(self, buffer_init, expected_head, expected_tail):
        buffer = RingBuffer(buffer_init)
        assert buffer.head == expected_head
        assert buffer.tail == expected_tail

    @pytest.mark.parametrize(
        "buffer_init, items_to_push, expected_length, expected_tail",
        [
            (None, [], 0, 3),
            (None, [1], 1, 0),
            (None, list(range(4)), 4, 3),
            (None, list(range(5)), 5, 4),
            (list(range(2)), list(range(2)), 4, 3),
            (list(range(5)), list(range(17)), 22, 21),
        ],
    )
    def test_push(self, buffer_init, items_to_push, expected_length, expected_tail):
        buffer = RingBuffer(buffer_init)
        for item in items_to_push:
            buffer.push(item)

        assert len(buffer) == expected_length
        assert buffer.tail == expected_tail

    @pytest.mark.parametrize(
        "buffer_init, items_to_enqueue, expected_length, expected_head",
        [
            (None, [], 0, 0),
            (None, [1], 1, 3),
            (None, list(range(3)), 3, 1),
            (list(range(2)), list(range(2)), 4, 2),
            (list(range(4)), list(range(3)), 7, 5),
        ],
    )
    def test_enqueue(self, buffer_init, items_to_enqueue, expected_length, expected_head):
        buffer = RingBuffer(buffer_init)
        for item in items_to_enqueue:
            buffer.enqueue(item)

        assert len(buffer) == expected_length
        assert buffer.head == expected_head

    @pytest.mark.parametrize(
        "buffer_init, pop_count, expected_length, expected_tail",
        [
            (55, 1, 0, 3),
            (list(range(1)), 1, 0, 3),
            (list(range(2)), 1, 1, 0),
            (list(range(10)), 5, 5, 4),
            (list(range(10)), 10, 0, 9),
        ],
    )
    def test_pop(self, buffer_init, pop_count, expected_length, expected_tail):
        buffer = RingBuffer(buffer_init)
        print(repr(buffer))
        for _ in range(pop_count):
            buffer.pop()

        assert len(buffer) == expected_length
        assert buffer.tail == expected_tail

    def test_scenario1(self):
        buffer = RingBuffer()

        for i in range(10):
            buffer.push(i)

        for _ in range(0, 5):
            buffer.deque()

        for i in range(10, 18):
            buffer.push(i)

        assert len(buffer) == 13
        assert buffer.head == 5
        assert buffer.tail == 1
        assert buffer.get_array() == list(range(5, 18))

    def test_scenario2(self):
        buffer = RingBuffer(list(range(10)))

        for _ in range(0, 5):
            buffer.deque()

        for i in range(10, 18):
            buffer.push(i)

        assert len(buffer) == 13
        assert buffer.head == 0
        assert buffer.tail == 12
        assert buffer.get_array() == list(range(5, 18))

    def test_scenario3(self):
        buffer = RingBuffer(list(range(16)))

        for _ in range(0, 7):
            buffer.deque()

        for i in range(16, 21):
            buffer.push(i)

        assert len(buffer) == 14
        assert buffer.head == 7
        assert buffer.tail == 4
        assert buffer.get_array() == list(range(7, 21))

    def test_scenario4(self):
        buffer = RingBuffer(list(range(16)))

        for _ in range(0, 7):
            buffer.deque()

        for i in range(16, 21):
            buffer.push(i)

        for i in reversed(range(5, 7)):
            buffer.enqueue(i)

        assert len(buffer) == 16
        assert buffer.head == 5
        assert buffer.tail == 4
        assert buffer.get_array() == list(range(5, 21))
