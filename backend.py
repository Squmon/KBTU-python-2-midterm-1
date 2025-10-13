import sqlite3
import utils
# когда будет понятно какие именно методы будут нужны, то тут поменяем
class backend:
    def __init__(self, path_to_database):
        self.pd = path_to_database
        self.conn = sqlite3.connect(path_to_database)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
        
    def __del__(self):
        self.close()