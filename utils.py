import os
import sqlite3
import types

class disposable_database:
    def __init__(self, name, save_mode = True):
        self.pd = name
        if os.path.exists(name):
            if save_mode:
                raise Exception(f"turn off save mode if you REALLY want to use this and destroy {name}")
            else:
                os.remove(name)
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.pd)
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        os.remove(self.pd)

class query_manager:
    def __init__(self, cursor, path_to_sqls):
        self.sqls = dict()
        self.cursor = cursor

        def create_wrap(name):
            def q(self, **kwargs):
                return self.cursor.execute(self.sqls[name], **kwargs)
            return q
        for d in os.listdir(path_to_sqls):
            if not d.endswith('.sql'):
                continue
            name = d[:-4]
            with open(os.path.join(path_to_sqls, d), 'r') as j:
                self.sqls[name] = j.read()
            dm = types.MethodType(create_wrap(name), self)
            setattr(self, name, dm)
