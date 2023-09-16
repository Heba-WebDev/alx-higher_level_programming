#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Replace with your MySQL database connection details
db_url = "mysql://root:Tigres4_titles-nino@localhost/dbme"

engine = create_engine(db_url)

# Create a MetaData object
metadata = MetaData()

# Reflect the 'test' table from the database
test_table = Table('test', metadata, autoload=True, autoload_with=engine)

# Create a connection and execute a SELECT query
with engine.connect() as connection:
    select_query = test_table.select()
    result = connection.execute(select_query)

    for row in result:
        print(row)

