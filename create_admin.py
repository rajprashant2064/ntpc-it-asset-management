import bcrypt
from database import connect_database


def create_admin():
    connection = connect_database()

    if connection is None:
        print("Database Connection Failed.")
        return

    cursor = None

    try:
        username = input("Enter Admin Username: ").strip()
        full_name = input("Enter Admin Full Name: ").strip()
        password = input("Enter Admin Password: ")

        if username == "" or full_name == "" or password == "":
            print("All fields are required.")
            return

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        cursor = connection.cursor()

        query = """
        INSERT INTO Users (
            Username,
            Password,
            Full_Name,
            Role
        )
        VALUES (%s, %s, %s, %s)
        """

        values = (
            username,
            hashed_password,
            full_name,
            "Admin"
        )

        cursor.execute(query, values)
        connection.commit()

        print("Admin Account Created Successfully!")

    except Exception as error:
        print("Error Creating Admin Account:")
        print(error)

    finally:
        if cursor is not None:
            cursor.close()

        if connection.is_connected():
            connection.close()


create_admin()