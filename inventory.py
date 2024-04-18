
"""
Author: EJ
Project 2
Date: 10/13 Updated 12/4
Description: This is the main method. It implements classes from the other
two files and combines them. This class uses user input to create and 
manage a database of computers in a database.
"""


import sqlite3
from computer import Linux, Windows
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

"""
    validate_ip function checks a user's inputted IP adress to see if it is a valid IP

    :param ip_address: The IP address of the computer. It is used to uniquely identify each computer in
    the database
    :return: NULL
"""
def validate_ip(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4 or any(not part.isdigit() or int(part) < 0 or int(part) > 255 for part in parts):
        return False
    return True

"""
    The main function allows the user to interact with a computer inventory database by adding,
    updating, removing, and listing computers.

    :return: NULL
"""
def create_table():
            c.execute('''
                CREATE TABLE IF NOT EXISTS computers(
                    ip_address TEXT,
                    year_purchase INTEGER,
                    operating_system TEXT,
                    space INTEGER
                )
            ''')
            conn.commit()
def main():
    # Begins a loop for user input
    while True:
        print("MENU")
        print("L List all computers in your inventory")
        print("A Add a computer")
        print("U Update a computer")
        print("R Remove a computer")
        print("Q Quit")
        choice = input("...your choice: ").lower()
        

        if choice == 'a':
            ip_address = input("Enter the computer’s IP address: ")
            # Checking for valid IP
            if not validate_ip(ip_address):
                print("Invalid IP address.")
                continue
            # Year input
            year_purchase = int(input("Enter the year purchase: "))
            # OS input
            operating_system = input("Enter the operating system: ")
            # Check for Windows or Linux
            if "windows" in operating_system.lower():
                c_drive_capacity = int(input("Enter the C drive capacity: ").split()[0])
                computer = Windows(ip_address, year_purchase, operating_system, c_drive_capacity)
            else:
                fs_capacity = int(input("Enter the file system capacity in Gb, do not include units: ").split()[0])
                computer = Linux(ip_address, year_purchase, operating_system, fs_capacity)
            
            # This is the code that inserts the computers information into the database. It does not insert the computer object itself.
            c.execute("INSERT INTO computers (ip_address, year_purchase, operating_system, space) VALUES (?, ?, ?, ?)",
                    (computer.ip_address, computer.year_purchase, computer.operating_system, computer.getSpace()))
            conn.commit()
            print("Computer added successfully.")


        elif choice == 'l':
            # Prints each row by using SELECT SQL method.
            print("IP adress\tYear Purchased\tOperating System\tStorage Space (Gb)")
            print("-"*74)
            for row in c.execute('SELECT * FROM computers ORDER BY year_purchase'):
                ip, year, os, storage = row
                print(f"{ip}\t{year}\t\t{os}\t\t{storage}")

        elif choice == 'u':
            # Updates any computer with new information abou the computer.
            while True:
                ip_address = input("Enter the computer’s IP address to update (or 'q' to quit): ")
                if ip_address.lower() == 'q':
                    break
                elif validate_ip(ip_address):
                    new_os = input("Enter the new operating system: ")
                    new_space = int(input("Enter the new space: ").split()[0])
                    c.execute("UPDATE computers SET operating_system = ?, space = ? WHERE ip_address = ?",
                            (new_os, new_space, ip_address))
                    conn.commit()
                    break
                else:
                    print("Invalid IP address. Please try again.")


        elif choice == 'r':
            # Removes the computer with inputted IP adress
            ip_address = input("Enter the computer’s IP address to remove: ")
            c.execute("DELETE FROM computers WHERE ip_address = ?", (ip_address,))
            conn.commit()

        elif choice == 'q':
            # Quits
            break

if __name__ == "__main__":
    create_table()
    main()
    conn.close()