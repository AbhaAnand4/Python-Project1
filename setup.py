#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from printip import __version__

setup(
    name="ip_print",
    version=__version__,
    description="Simple Python utility to print ip address",
    author="Abha Anand",
    author_email="anandabha6@gmail.com",
    url="https://github.com/AbhaAnand4/ip-print",
    packages=find_packages(include=['printip','printip*']),
    entry_points={'console_scripts': ['ip_print=printip.ip_print:main']}
)