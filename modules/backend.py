import sqlite3
import modules.utils as utils


class backend:
    def __init__(self, path_to_database, path_to_sqls = "./sql"):
        self.pd = path_to_database
        self.conn = sqlite3.connect(path_to_database)
        self.cursor = self.conn.cursor()
        self.qm = utils.query_manager(self.cursor, path_to_sqls, path_to_database)

    def close(self):
        self.conn.close()

    def all_students(self):
        columns = [row[1] for row in self.qm.get_columns().fetchall()]
        return [columns] + self.qm.all_students().fetchall()

    def get_student_by_id(self, student_id):
        columns = [row[1] for row in self.qm.get_columns().fetchall()]
        return [columns] + self.qm.get_students_by_name_or_id(name=None, id=student_id).fetchall()

    def get_students_by_name(self, student_name):
        columns = [row[1] for row in self.qm.get_columns().fetchall()]
        return [columns] + self.qm.get_students_by_name_or_id(name=student_name, id=None).fetchall()

    def __del__(self):
        self.close()