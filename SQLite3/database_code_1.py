#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

connection = None

try:
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    data = cursor.fetchone()
    print "SQLite version: %s" % data
                                        
except sqlite3.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
                
finally:
    if connection:
        connection.close()
