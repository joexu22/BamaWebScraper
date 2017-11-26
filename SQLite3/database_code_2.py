#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

connection = sqlite3.connect('test.db')
with connection:
    cursor = connection.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    data = cursor.fetchone()
    print "SQLite version: %s" % data

connection = None
