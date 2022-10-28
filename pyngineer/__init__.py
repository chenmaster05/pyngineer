from types import ModuleType

import __main__ as main


def _sin(x):
    return x


def _sinh(x):
    return x


def _cos(x):
    return 1


def _cosh(x):
    return 1


def _tan(x):
    return x    


def _tanh(x):
    return x


def _exp(x):
    return 3 ** x


_E = 3
_PI = 3
_TAU = 2 * _PI


def _pyngineerify(symbols, module_name=None):
    prefix = f"{module_name}." if module_name else ""
    for symbol in symbols:
        match symbol.lower():
            case "e":
                exec(f"main.{prefix}{symbol} = _E")
            case "pi":
                exec(f"main.{prefix}{symbol} = _PI")
            case "tau":
                exec(f"main.{prefix}{symbol} = _TAU")
            case "sin":
                exec(f"main.{prefix}{symbol} = _sin")
            case "sinh":
                exec(f"main.{prefix}{symbol} = _sinh")
            case "cos":
                exec(f"main.{prefix}{symbol} = _cos")
            case "cosh":
                exec(f"main.{prefix}{symbol} = _cosh")
            case "tan":
                exec(f"main.{prefix}{symbol} = _tan")
            case "tanh":
                exec(f"main.{prefix}{symbol} = _tanh")
            case "exp":
                exec(f"main.{prefix}{symbol} = _exp")


def init_engineer():
    non_modules = []
    local_symbols = dir(main).copy()
    for symbol in local_symbols:
        obj = eval(f"main.{symbol}")
        if type(obj) is ModuleType:
            if hasattr(obj, "__all__"):
                # _pyngineerify(obj.__all__, symbol)
                _pyngineerify(vars(obj), symbol)
            else:
                _pyngineerify(vars(obj), symbol)
        else:
            non_modules.append(symbol)

    _pyngineerify(non_modules)


if __name__ == "__main__":
    print("Oh HAIL Engineering!")
