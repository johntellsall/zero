# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

test_requirements = ["pytest"]

setup(
    name="zero",
    version="0.0.1",
    description="Unlimited local storage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="",
    author="Konstantin Schubert",
    packages=find_packages(),
    tests_require=test_requirements,
    install_requires=[
        "fusepy", "b2", "pyyaml", "portalocker",
    ] + test_requirements,
    include_package_data=True,
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "zero-fuse = zero.main:fuse_main",
            "zero-worker = zero.main:worker_main",
            "debug-delete-everything = zero.main:reset_all",
        ]
    },
)
