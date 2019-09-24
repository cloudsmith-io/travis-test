"""Cloudsmith Example Package.
"""
from __future__ import absolute_import, print_function

from setuptools import setup


setup(
    name="cloudsmith-python-example",
    version="100",
    url="https://cloudsmith.io",
    license="Apache License 2.0",
    author="Cloudsmith Ltd",
    author_email="support@cloudsmith.io",
    description="Cloudsmith: Be Awesome. Automate Everything.",
    py_modules=["cloudsmith_python_example"],
    entry_points={
        "console_scripts": [
            "cloudmsmith-python-example=cloudsmith_python_example:be_awesome"
        ]
    },
    keywords=["cloudsmith", "python", "example"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
