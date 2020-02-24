# holo
Holo is a library provides overload like cpp

## Installation

```py
pip install holo
```


## A Simple Example

```py
from holo import overload

@overload
def add(l, r):
    return l + r

@overload
def add(l):
    return l + 2

add(3)
#>5
add(3, 4)
#>7

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
f.add()
#>5
f.add(4)
#>7
```