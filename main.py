import webview
from backend import backend

class API:
    def __init__(self):
        self.be = backend("students.db")

    def get_all_students(self):
        return generate_table(self.be.all_students())

    def get_by_name(self, name):
        # Получение студентов по имени через backend
        return generate_table(self.be.qm.get_students_by_name_or_id(name=name, id=None).fetchall())

    def get_by_id(self, id):
        # Получение студентов по ID через backend
        return generate_table(self.be.qm.get_students_by_name_or_id(name=None, id=id).fetchall())

def generate_table(content):
    source = '<table border = "1">'
    for nr, row in enumerate(content):
        source += "<tr>"
        for col in row:
            if nr == 0:
                source += f"<th>{col}</th>"
            else:
                source += f"<td>{col}</td>"
        source += "</tr>"
    return source

if __name__ == '__main__':
    api = API()
    webview.create_window('GUI', 'index.html', js_api=api)
    webview.start()