import sqlite3
import requests
from xml.dom import minidom
from prettytable import PrettyTable


def create_kns_factions_db():
    """
    create sql database with all information on factions that run to the israeli knesset.
    """
    # request data
    database_url = 'http://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_Faction()'
    response = requests.get(database_url)

    # create database
    db = sqlite3.connect('my_database.db')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS KNS_Faction")
    cursor.execute('''
        CREATE TABLE KNS_Faction(
            Id     INTEGER   PRIMARY KEY, 
            Name   VARCHAR(50),
            KnessetNum  INTEGER, 
            StartDate DATETIME2,
            FinishDate  DATETIME2, 
            IsCurrent BIT,
            LastUpdatedDate DATETIME2)
    ''')

    # iterate on every faction in database
    data = minidom.parseString(response.content)
    factions = data.getElementsByTagName('m:properties')
    for faction in factions:
        # get all parameters and insert to database
        params = [elem.firstChild.nodeValue for elem in faction.childNodes]
        cursor.executemany('''
            INSERT INTO KNS_Faction(Id, Name, KnessetNum, StartDate, FinishDate, IsCurrent, LastUpdatedDate)
            VALUES(?,?,?,?,?,?,?)
        ''', [params])
        db.commit()

if __name__ == '__main__':
    # connect to database
    create_kns_factions_db()
    db = sqlite3.connect('my_database.db')
    cursor = db.cursor()

    # select all the factions that ran for the 16th Knesset
    cursor.execute('''SELECT * FROM KNS_Faction WHERE KnessetNum = 16''')
    result = cursor.fetchall()
    tab = PrettyTable([i[0] for i in cursor.description])
    tab.add_rows(result)
    print('all the factions that ran for the 16th Knesset')
    print(tab)

    db.close()
