import sqlite3
import utils
# когда будет понятно какие именно методы будут нужны, то тут поменяем
class backend:
    def __init__(self, path_to_database, path_to_sqls = "./sql"):
        self.pd = path_to_database
        self.conn = sqlite3.connect(path_to_database)
        self.cursor = self.conn.cursor()
        self.qm = utils.query_manager(self.cursor, path_to_sqls)

    def close(self):
        self.conn.close()

    def all_students(self):
        return self.qm.all_students()

    def __del__(self):
        self.close()