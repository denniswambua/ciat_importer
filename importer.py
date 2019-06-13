import xlrd

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

    def loader(self):
        sql_txt = None
        with open('db/scripts/tables.sql', 'r') as reader:
            sql_txt = reader.read()

        if sql_txt:

            with self.connection.cursor() as cursor:
                # execute SQL query using execute() method.
                cursor.execute(sql_txt)
                connection.commit()

            print("Table created")

    def insert_record(self, values):
        sql = 'insert into socio_monitorig_main ({}) values ("{}");'

        columns = ','.join(self.header)
        value = '","'.join(values) 
        insert_sql = sql.format(columns, value)
        print(insert_sql)
        with self.connection.cursor() as cursor:
            # execute SQL query using execute() method.
            cursor.execute(insert_sql)
            connection.commit()

            print("Record Inserted")

    def set_headers(self, sheet):
        self.header = []
        tmp_header = self.get_values(sheet, 0)

        for hh in tmp_header:
            hh = hh.replace("/", "_")
            self.header.append(hh)

    def get_values(self, sheet, index):
        values = []
        for i in range(sheet.ncols): 
            values.append(sheet.cell_value(0, i))

        return values

    def read_xls(self, loc):
        wb = xlrd.open_workbook(loc) 
        sheet = wb.sheet_by_index(0)
        
        self.set_headers(sheet)

        values = self.get_values(sheet, 1)

        self.insert_record(values)
        


if __name__ == "__main__":
    connection = Connection.get_instance()
    try:
        importer = CIATDataImporter(connection)
        #importer.loader()
        importer.read_xls("db/test.xlsx")
    finally:
        connection.close()
