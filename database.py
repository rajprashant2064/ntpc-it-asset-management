import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def connect_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="Ntpc_Asset_Management",
            use_pure=True
        )

        return connection

    except mysql.connector.Error as error:
        print("Database Connection Failed!")
        print(error)
        return None