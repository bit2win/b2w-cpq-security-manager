# import sqlite3

# from b2worm import db_instance
# from b2worm.schema import refresh


# def pytest_configure():
#     """
#     Configuration hook for pytest.
#     Create an empty SQLite DB with a preloaded SQL instruction from file.
#     """
#     db_instance.metadata.drop_all(db_instance.engine)
#     with open("./src/product_manager_api/v1/tests/initdb.sql", "r") as sql_file:
#         sql_script = sql_file.read()
#     db = sqlite3.connect("./test.db")
#     cursor = db.cursor()
#     cursor.executescript(sql_script)
#     db.commit()
#     db.close()
#     refresh()
