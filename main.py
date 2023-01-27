#Dette er SQL 3 oppgave

import sqlite3
import csv

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():

    c.execute('''CREATE TABLE IF NOT EXISTS postnummer (
        postnr INTEGER PRIMARY KEY,
        poststed TEXT NOT NULL,
        kommunenr INTEGER NOT NULL,
        kommunenavn TEXT NOT NULL,
        kategori TEXT NOT NULL,
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS kundeinfo (
        kundenr INTEGER PRIMARY KEY AUTOINCREMENT,
        fnavn TEXT NOT NULL,
        enavn TEXT NOT NULL,
        epost TEXT NOT NULL,
        adresse TEXT NOT NULL,
        postnr INTEGER NOT NULL,
        FOREIGN KEY (postnr) REFERENCES postnummer (postnr)
    )''')


def insert_data():
        with open('postnummer.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                c.execute('INSERT INTO postnummer (postnr, poststed, kommunenr, kommuenenav, kategori) VALUES (?, ?, ?, ?, ?)', row)
    
        with open('kundeinfo.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                c.execute('INSERT INTO kundeinfo (kundenr, fnavn, enavn, epost, adresse, postnr) VALUES (?, ?, ?, ?, ?, ?)', row)

create_table()
insert_data()