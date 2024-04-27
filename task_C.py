def validate_username(username):
    if len(username) >= 5 and username.isalnum():
        print("Valid username.")
    else:
        print("Invalid username.")

# Prompt user for input
username = input("Enter a username: ")
validate_username(username)
