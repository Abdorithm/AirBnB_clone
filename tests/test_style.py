import os
import unittest
import pycodestyle


class TestStyle(unittest.TestCase):
    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide()
        project_dir = '.'

        python_files = []
        for root, _, files in os.walk(project_dir):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))

        for python_file in python_files:
            result = style.check_files([python_file])
            errors = result.total_errors

            if errors != 0:
                print(f"violations in {python_file}: {errors} errors")

            self.assertEqual(errors, 0, f"violations in {python_file}")


if __name__ == '__main__':
    unittest.main()
