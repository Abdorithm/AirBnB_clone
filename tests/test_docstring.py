import unittest
import os
import importlib
import inspect


class TestDocstringsAll(unittest.TestCase):
    def test_module_docstrings(self):
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith(".py"):
                    module_name = os.path.splitext(file)[0]
                    module = importlib.import_module(module_name)
                    self.assertIsNotNone(
                            module.__doc__,
                            f"Module '{module_name}' has no documentation"
                        )

    def test_class_docstrings(self):
        for root, _, files in os.walk("path/to/your/project"):
            for file in files:
                if file.endswith(".py"):
                    module_name = os.path.splitext(file)[0]
                    module = importlib.import_module(module_name)
                    self.assertIsNotNone(
                            module.__doc__,
                            f"Module '{module_name}' has no documentation"
                        )

                    for name, obj in inspect.getmembers(module):
                        if inspect.isclass(obj):
                            self.assertIsNotNone(
                                    obj.__doc__,
                                    f"Class '{name}' has no documentation"
                                )

    def test_function_docstrings(self):
        for root, _, files in os.walk("path/to/your/project"):
            for file in files:
                if file.endswith(".py"):
                    module_name = os.path.splitext(file)[0]
                    module = importlib.import_module(module_name)

                    for name, obj in inspect.getmembers(module):
                        if inspect.isfunction(obj) or inspect.ismethod(obj):
                            self.assertIsNotNone(
                                    obj.__doc__,
                                    f"Function '{name}' has no documentation"
                                )


if __name__ == '__main__':
    unittest.main()
