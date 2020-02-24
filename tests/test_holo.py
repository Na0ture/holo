from holo import __version__
from holo import overload


def test_version():
    assert __version__ == "0.1.1"


def test_overload():
    @overload
    def add(l, r):
        return l + r

    @overload
    def add(l):
        return l + 2

    assert add(3) == 5
    assert add(3, 4) == 7

    class Bar:
        @overload
        def add(self, l):
            return l + 2

        @overload
        def add(self, l, r):
            return l + r

    b = Bar()
    assert b.add(3, 4) == 7
    assert b.add(3) == 5

    class Foo:
        def __init__(self, l):
            self.l = l

        @overload
        def add(self):
            return self.l + 2

        @overload
        def add(self, r):
            return self.l + r

    f = Foo(3)
    assert f.add() == 5
    assert f.add(4) == 7
