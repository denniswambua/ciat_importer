import pymysql.cursors
import os

from dotenv import load_dotenv

# Open database connection
load_dotenv()

DATABASE = os.getenv("DATABASE", "mariadb")
USERNAME = os.getenv("USERNAME", "root")
PASSWORD = os.getenv("PASSWORD", "test")
DB_NAME = os.getenv("DB_NAME", "test")

class Connection:
    @staticmethod
    def get_instance():
        connection = pymysql.connect(host=DATABASE,
                            user=USERNAME,
                            password=PASSWORD,
                            db=DB_NAME,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        return connection
