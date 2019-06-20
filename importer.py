import xlrd

from connection import Connection
from loader.baseloader import BaseLoader
from db import columns

class CIATDataImporter:
    def __init__(self, connection):
        self.connection = connection

        # confirm connection
        self.version()

    def version(self):
        # prepare a cursor object using cursor() method
        with self.connection.cursor() as cursor:

            # execute SQL query using execute() method.
            cursor.execute("SELECT VERSION()")
            connection.commit()

            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()
            print("Database version : {} ".format(data))

    def read_xls(self, loc):
        wb = xlrd.open_workbook(loc)
        main_sheet = wb.sheet_by_index(0)
        demographic_sheet = wb.sheet_by_index(1)
        seasons_sheet = wb.sheet_by_index(2)

        BaseLoader(connection, 'db/scripts/main.sql', 'main', columns.MAIN).handle(main_sheet)
        BaseLoader(connection, 'db/scripts/demographics.sql', 'demographics', columns.DEMOGRAPHIC).handle(demographic_sheet)
        BaseLoader(connection, 'db/scripts/season.sql', 'season', columns.SEASONS).handle(seasons_sheet)


if __name__ == "__main__":
    connection = Connection.get_instance()
    try:
        importer = CIATDataImporter(connection)
        importer.read_xls("db/data.xls") 
    finally:
        connection.close()