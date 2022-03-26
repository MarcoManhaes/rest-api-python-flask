import sqlite3

connection = sqlite3.connect(('pySqlite.db'))
cursor = connection.cursor()

sql_cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (\
                hotel_id text PROIIMARY KEY, nome text,\
                estrelas real, diaria real, cidade text)"

sql_cria_hoteis =   "INSERT INTO hoteis VALUES \
                    ('alpha', 'Alpha Hotel', 4.3, 420.34, 'Rio de Janeiro'),\
                    ('bravo', 'Bravo Hotel', 4.4, 380.90, 'Santa Catarina'),\
                    ('charlie', 'Charlie Hotel', 3.9, 320.20, 'Santa Catarina');"
    

cursor.execute((sql_cria_tabela))
cursor.execute((sql_cria_hoteis))

connection.commit()
connection.close()
