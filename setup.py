#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from setuptools import setup

__author__ = "Engine Bai"
__maintainer__ = "dhilipsiva"

setup(
    name="ac-messager",
    version="1.0.1.1",
    packages=["ac_messager", ],
    license='The MIT License (MIT) Copyright © 2017 Engine Bai.',
    description="A Python Facebook Messenger library",
    author="Engine Bai",
    author_email="enginebai@gmail.com",
    maintainer='dhilipsiva',
    maintainer_email='dhilipsiva@gmail.com',
    url="https://github.com/aircto/ac-messager",
    install_requires=[
        "requests"
    ],
)
