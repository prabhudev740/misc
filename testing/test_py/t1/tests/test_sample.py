from t1.sample import add

def test_add_num():
    assert add(1, 2) == 3

def test_add_str():
    assert add("a", "b") == "ab"

def test_add_list():
    assert add([1], [2, 3]) == [1, 2, 3]

class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"

    def test_add_list(self):
        assert add([1], [2, 3]) == [1, 2, 3]