from setuptools import setup, find_packages
from codecs import open
from os import path
import sys

setup(
    name='travis-test',
    version='0.0.1',
    description='This is a description',
    url='https://github.com/glasnt/travis-test',
    author='Katie McLaughlin',
    author_email='katie@glasnt.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages()
)
