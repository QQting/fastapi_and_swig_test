#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


wrapper_module = Extension('_rmt_py_wrapper',
                           sources=['example_wrap.c', 'example.c'],
                           include_dirs=['include'],
                           )

# $ python setup.py build_ext --inplace
setup (name = 'example',
       version = '0.1',
       author      = "Ting Chang<ting.chang@adlinktech.com>",
       description = """Simple swig example from docs""",
       ext_modules = [wrapper_module],
       py_modules = ["rmt_py_wrapper"],
       )