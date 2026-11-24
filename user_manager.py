"""Simple user management functions.

Users are stored in a plain Python list of dictionaries.
Each user looks like: {"id": 1, "name": "Alice", "email": "alice@example.com"}
"""


def validate_email(email):
    """Return True if the email looks valid, otherwise False."""
    if not isinstance(email, str):
        return False
    if "@" in email and "." in email:
        return True
    return False


def add_user(users, name, email):
    """Add a new user to the list and return the new user.

    Raises ValueError if the name is empty or the email is not valid.
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")
    if not validate_email(email):
        raise ValueError(f"Invalid email address: {email}")

    # IDs start at 1 and go up by one for every new user.
    new_id = len(users) + 1
    user = {"id": new_id, "name": name.strip(), "email": email}
    users.append(user)
    return user


def find_user_by_id(users, user_id):
    """Return the user with the given ID, or None if there is no such user."""
    if user_id < 1 or user_id > len(users):
        return None
    return users[user_id]
