import sqlite3
from zipfile import ZipFile

with ZipFile('Players_20.csv.zip', 'r') as zip:
    zip.printdir()
    zip.extractall()

file = open('players_20.csv', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines[1:]]

file.close()



for line in lines:
    player_data = line.split(',')

