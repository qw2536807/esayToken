#!/usr/bin/env python

import re
import setuptools

version = ""


setuptools.setup(
    name="esayToken",
    version="0.1.5",
    author="q2536807",
    author_email="616566665@qq.com ",
    description="esayTokenTest",
    long_description="esayTokenTest",
    url="http://example.com",
    install_requires=['crypto','pycryptodome'],
    packages=setuptools.find_packages(),
    include_package_data = True,
    platforms = "any"
)