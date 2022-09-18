import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# INTEGER required for auto-increment id
create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_users_table)

create_items_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_items_table)

connection.commit()

connection.close()