[Click here for English documentation](https://github.com/chenmaster05/pyngineer/blob/main/README.md)

# Pyngineer

可以满足所有工程学家Python需求的库！

此库在使用时会重新定义部分常量与函数从而更好地满足工程学家的需求。

## 使用样例

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

## 公开接口

```python
def init_engineer():
```

该函数将立刻重新定义所有与工程学用途有关的常量与函数。

## 安装指南

你需要

- Python 3.10 或更高。

然后，下载本仓库并在仓库根目录运行：
```
$ pip install .
```

## 开源许可证

该项目在*工程学家通用公共许可证v0x0*（*Engineer's GPL v0x0*）下进行开源。
