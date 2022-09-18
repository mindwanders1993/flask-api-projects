import sqlite3

# setting up database with the cursor method
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# create table
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# insert data into table
user = (1, 'biswa1', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'biswa2', 'asdf'),
    (3, 'biswa3', 'asdf'),
    (4, 'biswa4', 'asdf')
]
cursor.executemany(insert_query, users)

# select data from table
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


# save changes to disk data.db
connection.commit()

# close the connection
connection.close()