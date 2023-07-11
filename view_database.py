from functions.sql_handler import SQLHandler

db_path = 'database/kratom.db' # Provide path to database file

sql_handler = SQLHandler(db_path)
sql_handler.view_tables()

