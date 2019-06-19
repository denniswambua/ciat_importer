class BaseLoader:

    def __init__(self, connection, path, table_name, columns):
        self.connection = connection
        self.path = path
        self.table_name = table_name
        self.columns = columns

    def _prepare(self):
        columns = ','.join(self.header)
        value = '{}'
        self.insert_sql = f'insert into {self.table_name} ({columns}) values ("{value}");'

    def load_table(self):
        with open(self.path, 'r') as reader:
            sql_txt = reader.read()

            if sql_txt:
                with self.connection.cursor() as cursor:
                    # execute SQL query using execute() method.
                    cursor.execute(sql_txt)
                    self.connection.commit()

                    print(f"Table {self.table_name} created")

    def insert_record(self, values):
        value = '","'.join(values)
        insert_sql = self.insert_sql.format(value)
        print(insert_sql)
        with self.connection.cursor() as cursor:
            # execute SQL query using execute() method.
            cursor.execute(insert_sql)
            self.connection.commit()
            print("Record Inserted")

    def set_headers(self, sheet):
        self.header = []
        self.index = []

        for i in range(sheet.ncols):
            v = sheet.cell_value(0, i)
            if v in self.columns:
                self.header.append(v)
                self.index.append(i)

    def get_values(self, sheet, index):
        values = []
        for i in self.index:
            v = sheet.cell_value(index, i)
            values.append(str(v))

        return values

    def handle(self, sheet):
        try:
            self.load_table()
        except Exception as e:
            print(e)

        self.set_headers(sheet)
        self._prepare()

        no_of_rows = sheet.nrows
        for row in range(1, no_of_rows):
            value = self.get_values(sheet, row)
            self.insert_record(value)
