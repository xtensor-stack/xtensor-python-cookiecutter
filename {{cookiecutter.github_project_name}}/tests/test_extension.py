import {{ cookiecutter.python_package_name }} as m
from unittest import TestCase
import numpy as np


class ExampleTest(TestCase):

    def test_example1(self):
        self.assertEqual(4, m.example1([4, 5, 6]))

    def test_example2(self):
        x = np.array([[0., 1.], [2., 3.]])
        res = np.array([[2., 3.], [4., 5.]])
        y = m.example2(x)
        np.testing.assert_allclose(y, res, 1e-12)

    def test_vectorize(self):
        x1 = np.array([[0, 1], [2, 3]])
        x2 = np.array([0, 1])
        res = np.array([[ 1.               ,  1.381773290676036],
                        [ 1.909297426825682,  0.681422313928007]])
        y = m.vectorize_example1(x1, x2)
        np.testing.assert_allclose(y, res, 1e-12)

    def test_readme_example1(self):
        v = np.arange(15).reshape(3, 5)
        y = m.readme_example1(v)
        np.testing.assert_allclose(y, 1.2853996391883833, 1e-12)

