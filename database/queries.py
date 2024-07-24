class Queries:
    CREATE_TABLE_REVIEW = '''
    CREATE TABLE IF NOT EXISTS review(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    food TEXT,
    opinion TEXT)'''

