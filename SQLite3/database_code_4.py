#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

cars = [
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
]

connection = sqlite3.connect('test.db')
with connection:
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Cars")
    cursor.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cursor.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
