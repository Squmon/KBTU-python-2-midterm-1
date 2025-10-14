from utils import disposable_database, query_manager


with disposable_database("OutHolyDataBase.db") as conn:
    cursor = conn.cursor()
    qm = query_manager(cursor, 'sql')
    qm.create_tables() ##dsdsds
    qm.insert_student(fullname = 'Vlad Lyashenkov')
    qm.insert_student(fullname = 'Ilya Lyashenkov')
    print(qm.all_students().fetchall())