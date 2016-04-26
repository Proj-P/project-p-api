#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

import re
import ast
from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('api/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='project-p-api',
    version=version,
    description='This API is part of Project P and provides an interface which'
                ' other applications can use to access monitored data.',
    url='https://github.com/Proj-P/api',
    license='MIT',
    author='Steven Oud',
    author_email='soud@protonmail.com',
    long_description=long_description,
    packages=['api', 'api.visits'],
    include_package_data=True,
    install_requires=[
        'Flask==0.10.1',
        'Flask-SQLAlchemy==2.1',
        'Flask-WTF==0.12',
        'itsdangerous==0.24',
        'MarkupSafe==0.23',
        'SQLAlchemy==1.0.12',
        'Werkzeug==0.11.8',
        'WTForms==2.1'
    ],
    entry_points = {
        'console_scripts': [
            'run-server = api.run:main',
            'generate-token = scripts.generate_token:main'
        ]
    }
)