import sqlite3
# connect to database if file doesnt exist yet
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
# id INTEGER PRIMARY KEY,
# name TEXT,
# enrollmentdate DATE
# )''')

# cursor.execute('''INSERT INTO Students (name, enrollmentdate) VALUES ('Alice', '2024-07-03')''')
# cursor.execute('''INSERT INTO Students (name, enrollmentdate) VALUES ('Bob', '2024-07-05')''')
# conn.commit() # Save changes
# cursor.execute("SELECT * FROM Students")
# results = cursor.fetchall() # Fetch all records
# for row in results:
#     print(row)
# conn.close() # Close the connection when done


while True:
    print("1. Type 1 to Insert data.")
    print("2. Type 2 to Output all data.")
    print("3. Type 3 to Delete data.")
    print("4. Type 4 to Update data.")
    print("5. Type 5 to exit the program.")
    cmd = int(input("Type here: "))
    print("---")
    if cmd == 1:
        name = input("Input student's name: ")
        date = input("Input enrollment's date: ")
        cursor.execute(f"INSERT INTO Students (name, enrollmentdate) VALUES ('{name}', '{date}')")
        conn.commit() # Save changes

    if cmd == 2:
        cursor.execute("SELECT * FROM Students")
        results = cursor.fetchall() # Fetch all records
        for row in results:
            print(row)

    if cmd == 3:
    # Delete data
        print("1. Delete by ID.")
        print("2. Delete by Name.")
        delete_cmd = int(input("Choose delete method: "))
        if delete_cmd == 1:
            record_id = int(input("Enter the ID of the record to delete: "))
            cursor.execute("DELETE FROM Students WHERE id = ?", (record_id,))
        elif delete_cmd == 2:
            name = input("Enter the name of the record to delete: ")
            cursor.execute("DELETE FROM Students WHERE name = ?", (name,))
        conn.commit()  # Save changes
        print("Record deleted successfully.")


    if cmd == 4:
        # Update data
        print("1. Update Name.")
        print("2. Update Enrollment Date.")
        update_cmd = int(input("Choose update method: "))
        record_id = int(input("Enter the ID of the record to update: "))
        
        if update_cmd == 1:
            new_name = input("Enter the new name: ")
            cursor.execute("UPDATE Students SET name = ? WHERE id = ?", (new_name, record_id))
        elif update_cmd == 2:
            new_date = input("Enter the new enrollment date: ")
            cursor.execute("UPDATE Students SET enrollmentdate = ? WHERE id = ?", (new_date, record_id))
        
        conn.commit()  # Save changes
        print("Record updated successfully.")

    if cmd == 5:
        break
    print("---")
conn.close() # This is like putting back the water bottle lid to prevent the water from spilling

