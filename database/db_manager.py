import sqlite3


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores(
            username TEXT,
            game TEXT,
            score INTEGER
        )
        """)

        self.conn.commit()

    # -------- AUTH --------
    def register(self, username, password):
        try:
            self.cursor.execute(
                "INSERT INTO users VALUES (?, ?)",
                (username, password)
            )
            self.conn.commit()
            return True
        except:
            return False

    def login(self, username, password):
        self.cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        return self.cursor.fetchone()

    # -------- SCORES --------
    def save_score(self, username, game, score):
        self.cursor.execute(
            "INSERT INTO scores VALUES (?, ?, ?)",
            (username, game, score)
        )
        self.conn.commit()

    def get_user_stats(self, username):
        self.cursor.execute(
            "SELECT game, score FROM scores WHERE username=?",
            (username,)
        )
        return self.cursor.fetchall()

    def get_leaderboard(self):
        self.cursor.execute(
            "SELECT username, game, MAX(score) FROM scores GROUP BY username, game"
        )
        return self.cursor.fetchall()
