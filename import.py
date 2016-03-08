import csv, sqlite3

conn = sqlite3.connect('C:/Users/David/Desktop/fyp/rep3Party.db')
c = conn.cursor()
#c.execute('''DROP TABLE info''')
c.execute('''CREATE TABLE IF NOT EXISTS info
          (Name, Friend, Party)''')

with open('C:/Users/David/Desktop/fyp/partiesRep.csv','rb') as fin: 
    dr = csv.reader(fin) # comma is default delimiter
    to_db = [(i[0], i[1], i[2]) for i in dr]

c.executemany("INSERT INTO info (Name, Friend, Party)  VALUES (?, ?, ?);", to_db)
conn.commit()