from connection import Connection

class CIATDataImporter:
    def __init__(self, connection):
        self.connection = connection

    def version(self):
        # prepare a cursor object using cursor() method
        with self.connection.cursor() as cursor:

            # execute SQL query using execute() method.
            cursor.execute("SELECT VERSION()")
            connection.commit()

            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()
            print("Database version : {} ".format(data))




if __name__ == "__main__":
    connection =  Connection.get_instance()
    try:
        importer = CIATDataImporter(connection)
        importer.version()
    finally:
        connection.close()