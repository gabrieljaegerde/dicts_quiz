from solutions.dicts import get_value, remove_key

def test_get_value():
    assert get_value({"a": 1, "b": 2}, "a") == 1
    assert get_value({"a": 1, "b": 2}, "b") == 2
    assert get_value({"a": 1, "b": 2}, "c") is None

def test_remove_key():
    assert remove_key({"a": 1, "b": 2}, "a") == {"b": 2}
    assert remove_key({"a": 1, "b": 2}, "b") == {"a": 1}
    assert remove_key({"a": 1, "b": 2}, "c") == {"a": 1, "b": 2}