#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name='swiftwind-heroku',
    version=open('VERSION').read().strip(),
    # Your name & email here
    author='Adam Charnock',
    author_email='adam@adamcharnock.com',
    # If you had swiftwind_heroku.tests, you would also include that in this list
    packages=find_packages(),
    # Any executable scripts, typically in 'bin'. E.g 'bin/do-something.py'
    scripts=[],
    # REQUIRED: Your project's URL
    url='https://github.com/adamcharnock/swiftwind-heroku',
    # Put your license here. See LICENSE.txt for more information
    license='MIT',
    # Put a nice one-liner description here
    description='Swiftwind for Heroku Deployment',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[
        'swiftwind',
        'dj_database_url',
    ],
    # Ensure we include files from the manifest
    include_package_data=True,
)
