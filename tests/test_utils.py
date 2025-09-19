import pytest
from tt_gutenberg.utils import sort_by_count


def test_sort_by_count_basic():
    d = {"a": 2, "b": 5, "c": 1}
    assert sort_by_count(d) == ["b", "a", "c"]


def test_sort_by_count_tie_break():
    d = {"alice": 3, "bob": 3, "charlie": 2}
    assert sort_by_count(d) == ["alice", "bob", "charlie"]


def test_sort_by_count_empty():
    assert sort_by_count({}) == []


def test_sort_by_count_invalid_input_type():
    with pytest.raises(TypeError):
        sort_by_count([1, 2, 3])


def test_sort_by_count_invalid_value_type():
    with pytest.raises(TypeError):
        sort_by_count({"a": "two", "b": 1})
