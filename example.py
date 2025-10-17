from utils import disposable_database, query_manager
import random as rd

with disposable_database("OutHolyDataBase.db") as conn:
    cursor = conn.cursor()
    qm = query_manager(cursor, 'sql')
    qm.create_tables() ##dsdsds
    ##adding names and surnames
    names = """Aruzhan, Aigerim, Dias, Nursultan, Alina, Madina, Yerassyl, Dana,
Vladimir, Arman, Sanzhar, Dmitry, Amina, Laura, Miras, Aliya,
Nikita, Askar, Kamila, Ruslan, Azhar, Samat, Zarina, Yernar,
Alexandra, Timur, Nurlan, Mariya, Aruzhan, Roman, Yerkebulan,
Valentina, Dias, Ayan, Polina, Baglan, Alibek, Yulia, Renat,
Anastasia, Azamat, Aray, Aruzhan, Bota, Adil, Olzhas, Svetlana,
Kairat, Diana, Vladislav, Assel""" 
surnames = """"Smirnov, Akhmetov, Ivanova, Mukhamedzhanov, Kim, Nazarova, Petrov,
Suleimenova, Orlov, Tulegenov, Serikova, Volkov, Iskakov, Sidorov,
Kuznetsova, Yessimov, Karpov, Temirbaeva, Nikolaev, Kassymov,
Fedorov, Zhumabekov, Andreeva, Ospanova, Morozov, Abdrakhmanova,
Lebedev, Sadykov, Rakhimova, Makarov, Nurpeisov, Kolesnikova,
Ivanov, Baimukhanov, Popova, Kenzhegulov, Kovalenko, Sharipova,
Sokolov, Imanbekov, Vasiliev, Abdullaeva, Loginov, Karimov,
Kuzmina, Turganbekov, Pavlova, Bekturov, Gromova, Orazov"""
#turning names and surnames into the list so that we could use random.choice
firstnames = [name.strip() for name in names.split(",") if name.strip()]
lastnames = [surname.strip() for surname in surnames.split(",") if surname.strip()]
    #creating 50 students using random names and surnames and random grades from 40 to 100
for i in range(50):
        first = rd.choice(firstnames)
        last = rd.choice(surnames)
        fullname = f"{first} {last}"
        math = rd.randint(40, 100)
        physics = rd.randint(40, 100)
        duck_science = rd.randint(40, 100)
        ict = rd.randint(40, 100)
        english = rd.randint(40, 100)
        #inserting students into the table
        qm.insert_student(fullname=fullname, Math=math, Physics=physics,
                          DuckScience=duck_science, ICT=ict, English=english)
    #fetching and printing all students
for student in qm.all_students().fetchall():
        print(student)


