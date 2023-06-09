import gspread
import random
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fortunecookiepp3')

worksheet = SHEET.sheet1

fortunes = worksheet.col_values(1)

def get_fortune():
    """
    Selects a random fortune from the list of fortunes.
    
    """
    return random.choice(fortunes)

def print_fortune_cookie():
    """
    Prints a visual representation of a fortune cookie.
    
    """
    print("  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("  ┃                             ┃")
    print("  ┃       Fortune Cookie        ┃")
    print("  ┃                             ┃")
    print("  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

def get_valid_input(prompt, valid_choices):
    """
    Prompts the user for input until a valid input is provided.
    
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid input. Please try again.")

def get_valid_name(prompt):
    """
    Prompts the user for a valid name containing only letters.
    
    """
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        else:
            print("Please enter a valid name containing only letters.")

def save_name_and_fortune_in_sheet(name, fortune):
    """
    Saves the user's name and fortune in the first empty cell of column 10.
    
    """
    for i in range(1, 301):
        cell_value = worksheet.cell(i, 10).value
        if not cell_value:
            worksheet.update_cell(i, 10, f"{name}: {fortune}")
            break

print_fortune_cookie()
print("Hello, please enter your name to get your fortune:")
name = get_valid_name("Name: ")

while True:
    fortune = get_fortune()
    print(f"\n{name}, your fortune is:\n")
    print(fortune)
    save_name_and_fortune_in_sheet(name, fortune)

    another_fortune = get_valid_input("Do you want to get another fortune? (y/n): ", ["y", "n"])
    if another_fortune != "y":
        print("\nLive long & prosper.")
        break