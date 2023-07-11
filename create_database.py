from functions.sql_handler import SQLHandler

db_file = 'database/kratom.db' # Provide path to database file

sql_handler = SQLHandler(db_file)
sql_handler.create_user_table()