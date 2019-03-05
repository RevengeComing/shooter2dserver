#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="shooter2d",
    version="0.0.1",
    description="shooter2d",
    author="shooter2d Team",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'shooter2d = shooter2d.cmd.main:cli',
        ],
    },

)