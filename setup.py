#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyalphaclock',
    version='0.1',
    description='Python library for interacting with the Alpha Clock Five',
    author='Anastasis Germanidis',
    author_email='agermanidis@gmail.com',
    url='https://github.com/agermanidis/pyalphaclock',
    packages=['pyalphaclock'],
    install_requires=[
        'pyserial>=2.7'
    ],
    license=open("LICENSE").read()
)
