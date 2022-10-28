[中文文档请点此处](https://github.com/chenmaster05/pyngineer/blob/main/README-zh_CN.md)

# Pyngineer

The package that suits all Engineer's Python needs!

This package redefines constants and functions for practical Engineering usage upon use.

## Example

```python
import math

import pyngineer
import scipy
import sympy

pi = 3.14

pyngineer.init_engineer()

print(scipy.pi)
# 3

print(sympy.E)
# 3

print(pi)
# 3

print(math.tau)
# 6
```

## Public API

```python
def init_engineer():
```

This function immediately redefines all relevant constants and functions for engineering purposes.

## Installation Instructions

You'll need:

- Python 3.10 or above.

Then, download this repository and run
```
$ pip install .
```
at the repository's root directory.

## License

This project is open-source under the *Engineer's GPL v0x0*.
