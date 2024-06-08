# service.py
import base64
from db.DatabaseConfig import create_connection

class Service:
    def __init__(self):
        self.conn = create_connection()

    def register_user(self, name, email, password):
        encoded_password = base64.b64encode(password.encode('ascii'))
        query = "INSERT INTO EA.USER (NAME, EMAIL, PASSWORD) VALUES (%s, %s, %s);"
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, (name, email, encoded_password))
            self.conn.commit()
            return {"message": "User registered successfully"}
        finally:
            cursor.close()

    def get_all_users(self):
        query = "SELECT * FROM EA.USER;"
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        finally:
            cursor.close()
