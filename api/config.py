# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

import os

HOST = '0.0.0.0'
PORT = 8080

# Debug state
DEBUG = True

# Application root directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Database (sqlite) configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True