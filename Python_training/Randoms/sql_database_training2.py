
import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

    # this is the first thing to do (create a table first) before jumping into insertion. And after creating the table, you can comment 
                                                                                                    # out this block of code
# cursor.execute('''CREATE TABLE Books (
# id INTEGER PRIMARY KEY,
# book_title TEXT,
# author TEXT,
# publication_year DATE
# )''')



while True:
    print('1. Insert new book: ')
    print('2. Output all books: ')
    print('3. Search by title: ')
    print('4. Search by author: ')
    print("5. Type 5 to Quit")
    cmd = int(input('Type here: '))

    if cmd == 1:
        new_book_title = input('New book title: ')
        new_author = input ('Author name: ')
        publication_year = int(input('Publication year: '))
        cursor.execute(f'INSERT INTO Books(book_title, author, publication_year) VALUES ("{new_book_title}","{new_author}","{publication_year}")')
        conn.commit()

    if cmd ==2:
        cursor.execute("SELECT * FROM Books")
        results = cursor.fetchall()
        for row in results:
            print(row)

    if cmd == 3:
        book_title = input('Search book title here: ')
        cursor.execute('SELECT * FROM Books WHERE book_title LIKE?',("%"+ book_title +"%",))# The ? acts as a placeholder for the ,("%"+ book_title +"%",)
                                    #Using f-strings with cursor.execute for SQL queries makes the application vulnerable to SQL injection attacks.
        result_book_title = cursor.fetchall()
        if result_book_title:
            for titles in result_book_title:
                print(titles)
        else:
            print('No matching found')

    if cmd == 4:
        author_name = input('Search author name here: ')
        cursor.execute('SELECT * FROM Books WHERE author LIKE?',("%"+ author_name +"%",))# The ? acts as a placeholder for the ,("%"+ book_title +"%",)
        result_author_name = cursor.fetchall()
        if result_author_name:
            for name in result_author_name:
                print(name)
        else:
            print('No matching found')
    if cmd == 5:
        break
    print("---")
conn.close()