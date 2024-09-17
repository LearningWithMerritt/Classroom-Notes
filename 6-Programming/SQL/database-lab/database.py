import sqlite3

# Connect to database
connection = sqlite3.connect("my-database.db")


#Create a cursor
c = connection.cursor()


# Create a Table

c.execute("CREATE TABLE users (first_name text, last_name text,email text)")
#sqlite datatypes: NULL, INTEGER, REAL, TEXT, BLOB

c.execute("INSERT INTO users VALUES ('First', 'Last', 'example@email.com)")

#Commit our command
connection.commit()

#Close our connection
connection.close()