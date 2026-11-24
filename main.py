"""Demo script showing how user_manager.py works."""

from user_manager import add_user, find_user_by_id, validate_email


def main():
    users = []

    print("--- Adding users ---")
    add_user(users, "Alice", "alice@example.com")
    add_user(users, "Bob", "bob@example.com")
    add_user(users, "Carol", "carol@example.com")
    for user in users:
        print(user)

    print("\n--- Finding users by ID ---")
    for user_id in (1, 2, 3, 10):
        found = find_user_by_id(users, user_id)
        if found:
            print(f"ID {user_id}: {found['name']} ({found['email']})")
        else:
            print(f"ID {user_id}: not found")

    print("\n--- Validating emails ---")
    for email in ("dave@example.com", "not-an-email", "eve@example"):
        print(f"{email!r} valid? {validate_email(email)}")

    print("\n--- Trying to add a user with a bad email ---")
    try:
        add_user(users, "Frank", "frank-at-example.com")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
