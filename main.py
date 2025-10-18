import webview
from modules.backend import backend

class API:
    def __init__(self):
        self.be = backend("students.db")

    def get_all_students(self):
        return generate_table(self.be.all_students(), ['mean', 'grade'])

    def get_by_name(self, name):
        return generate_table(self.be.get_students_by_name(name), ['mean', 'grade'])

    def get_by_id(self, id):
        return generate_table(self.be.get_student_by_id(id), ['mean', 'grade'])

def generate_table(content, other_colums = None):
    if other_colums is not None:
        content[0] += other_colums
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
    webview.create_window('GUI', 'sources/index.html', js_api=api)
    webview.start()