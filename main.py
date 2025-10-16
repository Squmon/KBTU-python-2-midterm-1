import random
import webview

class API:
    def get_all_students(self):
        return generate_table(
            [['student name', 'student_id', 'sub1']] + [[random.randrange(0, 9) for _ in range(3)] for _ in range(10)]
        )
    
    def get_by_name(self, name):
        return generate_table(
            [['student name', 'student_id', 'sub1']] + [[name]] + [[random.randrange(0, 9) for _ in range(2)] for _ in range(10)]
        )
    
    def get_by_id(self, id):
        id = int(id)
        return generate_table(
            [['student name', 'student_id', 'sub1', 'sub2']] + [["ilya"] ]+ [[id]] + [[random.randrange(0, 9) for _ in range(2)] for _ in range(10)]
        )

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