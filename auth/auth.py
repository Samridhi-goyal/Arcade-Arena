from database.db_manager import DBManager

db = DBManager()


def register_user(username, password):
    # Basic validation
    if not username or not password:
        return False, "Username and password cannot be empty"

    # Register user
    success = db.register(username, password)

    if success:
        return True, "Registration successful"
    else:
        return False, "User already exists"


def login_user(username, password):
    # Basic validation
    if not username or not password:
        return False, "Username and password cannot be empty"

    # Login check
    success = db.login(username, password)

    if success:
        return True, "Login successful"
    else:
        return False, "Invalid credentials"

