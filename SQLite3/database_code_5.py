#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

cars = [
    'Audi',
    'Mercedes',
    'Skoda',
    'Volvo',
    'Bentley',
    'Hummer',
    'Volkswagen'
    ]

connection = sqlite3.connect('test.db')

with connection:
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Cars")
    cursor.execute("CREATE TABLE Cars(Name TEXT PRIMARY KEY)")
    for car in cars:
        print car
        cursor.execute("INSERT INTO Cars VALUES (?)", [car])
    connection.commit()
