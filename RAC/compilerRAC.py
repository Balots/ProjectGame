import os
import sys
import importlib.util


currDir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, currDir)


class ExportModule:
    def __init__(self):
        self._AG = {}  # Все графические элементы
        for module in os.listdir(currDir):
            if (
                    module == '__init__.py' or
                    module == 'KindObjectArc.py' or
                    module == 'compilerRAC.py' or
                    module[-3:] != ".py"): continue
            self._AG[module[:-3]] = __import__(module[:-3])
        del module

    @property
    def AG(self):
        return self._AG


def check_module(module_name):
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module not found.'.format(module_name))
        return None
    else:
        return module_spec


def import_module(module_spec):
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def import_sources(module_name):
    module_file_path = module_name.__file__
    module_name = module_name.__name__

    module_spec = importlib.util.spec_from_file_location(
        module_name, module_file_path
    )
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)


if __name__ == '__main__':
    print('PROTECT')
