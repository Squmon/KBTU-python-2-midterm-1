from utils import disposable_database, query_manager


with disposable_database("OutHolyDataBase.db") as conn:
    cursor = conn.cursor()
    qm = query_manager(cursor, 'sql')
    qm.create_tables()
    qm.insert_student(fullname = 'Vlad Lyashenkov', age = 19)
    qm.insert_student(fullname = 'Ilya Lyashenkov', age = 12)
    print(qm.all_students().fetchall())