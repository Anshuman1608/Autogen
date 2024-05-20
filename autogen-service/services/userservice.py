import base64
from db.DatabaseConfig import create_connection

class Service:
    def __init__(self, name, email, password):
        self.name = name
        self.password = password
        self.email = email
        self.conn = create_connection()

    def register_user(self,name,email,password):
        encoded_password=base64.b64encode(password.encode('ascii'))
        query = "INSERT INTO EA.USER (NAME, EMAIL, PASSWORD) VALUES (%s, %s, %s);"
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, (name, email, encoded_password))
            self.conn.commit()
            return 0
        finally:
            cursor.close()