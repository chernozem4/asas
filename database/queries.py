class Queries:
    CREATE_COMMENT_TABLE = """
    CREATE TABLE IF NOT EXISTS review_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        visit_date INTEGER,
        instagram_username TEXT,
        food_rating TEXT,
        cleanliness_rating TEXT,
        extra_comments TEXT
    )
    """

