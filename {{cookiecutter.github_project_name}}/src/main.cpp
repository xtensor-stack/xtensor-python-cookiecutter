#include "pybind11/pybind11.h"

#include "xtensor/xmath.hpp"
#include "xtensor/xarray.hpp"

#define FORCE_IMPORT_ARRAY
#include "xtensor-python/pyarray.hpp"
#include "xtensor-python/pyvectorize.hpp"

#include <iostream>
#include <numeric>
#include <cmath>

namespace py = pybind11;

// Examples

inline double example1(xt::pyarray<double> &m)
{
    return m(0);
}

inline xt::pyarray<double> example2(xt::pyarray<double> &m)
{
    return m + 2;
}

// Readme Examples

inline double readme_example1(xt::pyarray<double> &m)
{
    auto sines = xt::sin(m);
    return std::accumulate(sines.cbegin(), sines.cend(), 0.0);
}

// Vectorize Examples

inline double scalar_func(double i, double j)
{
    return std::sin(i) + std::cos(j);
}

// Python Module and Docstrings

PYBIND11_PLUGIN({{ cookiecutter.python_package_name }})
{
    xt::import_numpy();

    py::module m("{{ cookiecutter.python_package_name }}", R"docu(
        {{ cookiecutter.project_short_description }}

        .. currentmodule:: {{ cookiecutter.python_package_name }}

        .. autosummary::
           :toctree: _generate

           example1
           example2
           readme_example1
           vectorize_example1
    )docu");

    m.def("example1", example1, "Return the first element of an array, of dimension at least one");
    m.def("example2", example2, "Return the the specified array plus 2");

    m.def("readme_example1", readme_example1, "Accumulate the sines of all the values of the specified array");

    m.def("vectorize_example1", xt::pyvectorize(scalar_func), "Add the sine and and cosine of the two specified values");

    return m.ptr();
}
