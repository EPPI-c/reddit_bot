import sqlite3


def get_db(self, name='database.db', script_path='tables.sql'):
    self.conn = sqlite3.connect(name)
    self.cursor = self.conn.cursor()
    with open(script_path, 'r') as f:
        self.cursor.executescript(f.read())