import pandas as pd
from modules.backend import backend

def display_table(data):
 if not data or len(data) <= 1:
  print("\nNo student records found.")
  return
 
 columns = data[0]
 rows = data[1:]
 
 if rows and len(rows[0]) != len(columns):
  columns = [f"Column_{i}" for i in range(len(rows[0]))]
 
 df = pd.DataFrame(rows, columns=columns)
 print(df.to_string(index=False))


def save_table_to_file(data, output_file='results.txt'):
 if not data or len(data) <= 1:
  print("\nNo student records found.")
  return
 
 columns = data[0]
 rows = data[1:]
 
 if rows and len(rows[0]) != len(columns):
  columns = [f"Column_{i}" for i in range(len(rows[0]))]
 
 df = pd.DataFrame(rows, columns=columns)
 
 with open(output_file, 'w') as f:
  f.write(df.to_string(index=False))
 
 print(f"Results saved to {output_file}")


def show_help():
 print("\n=== Student Management System ===")
 print("Commands:")
 print("  display - Display all students")
 print("  search  - Search student by name or ID")
 print("  save    - Save students to file")
 print("  help    - Show this help message")
 print("  exit    - Exit program")
 print("=================================\n")


def main():
 print("Welcome to Student Management System!")
 database_path = input("Enter database path: ")
 
 db = backend(database_path)
 show_help()
 
 while True:
  command = input("Enter command: ").strip().lower()
  
  if command == 'exit':
   db.close()
   break
  
  elif command == 'help':
   show_help()
  
  elif command == 'display':
   data = db.all_students()
   display_table(data)
  
  elif command == 'search':
   search_type = input("Search by (1) ID or (2) Name? Enter 1 or 2: ").strip()
   
   if search_type == '1':
    student_id = input("Enter student ID: ").strip()
    if student_id.isdigit():
     data = db.get_student_by_id(int(student_id))
     display_table(data)
    else:
     print("Invalid ID. Please enter a number.")
   
   elif search_type == '2':
    student_name = input("Enter student name: ").strip()
    if student_name:
     data = db.get_students_by_name(student_name)
     display_table(data)
    else:
     print("Name cannot be empty.")
   
   else:
    print("Invalid option. Enter 1 or 2.")
  
  elif command == 'save':
   output_file = input("Enter output file name (press Enter for 'results.txt'): ").strip()
   if not output_file:
    output_file = 'results.txt'
   data = db.all_students()
   save_table_to_file(data, output_file)
  
  else:
   print(f"Unknown command: '{command}'. Type 'help' for available commands.")


if __name__ == "__main__":
 main()