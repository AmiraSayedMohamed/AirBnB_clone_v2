import sys
from models import storage, amenity, city, review, state, user
from utils import get_user_input, display_menu

def main():
    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == 'q':
            print("Exiting AirBnB Clone...")
            sys.exit(0)
        elif choice == '1':  # Create a user (creative: add user verification)
            username = get_user_input("Enter username: ")
            email = get_user_input("Enter email: ")
            password = get_user_input("Enter password: ", hide_input=True)
            # Implement user verification logic (e.g., email confirmation)
            new_user = user.User(email=email, password=password, username=username)
            storage.new(new_user)
            storage.save()
            print(f"User {username} created successfully!")
        # ... other functionalities (listing creation, search, etc.)

if __name__ == "__main__":
    main()

