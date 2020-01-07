import json
from connection import Connection


def run_sql(connection, sql):
    with connection.cursor() as cursor:
        # execute SQL query using execute() method.
        cursor.execute(sql)
        connection.commit()


def load_table(connection):
    with open("db/form.sql", "r") as reader:
        sql_txt = reader.read()

        if sql_txt:
            run_sql(connection, sql_txt)


def load_data(connection, data):
    insert_sql = f"""
            insert into Feedgap_datacollection_forms_Tanzania_1st_sampling_v2 (
                xform_data_id,
                xform_id,
                edited,
                status,
                version,
                data,
                duration,
                media_count,
                total_media,
                submitted_by,
                submission_time
            ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    with connection.cursor() as cursor:
        for d in data:
            data_id = d["_id"]
            xform_id = d["_xform_id"]
            edited = d["_edited"]
            status = d["_status"]
            version = d["_version"]
            json_data = json.dumps(d)
            duration = d["_duration"]
            media_count = d["_media_count"]
            total_media = d["_total_media"]
            submitted_by = d["_submitted_by"]
            submission_time = d["_submission_time"]

            table_name = d["_xform_id_string"]

            insert_values = [
                data_id,
                xform_id,
                edited,
                status,
                version,
                json_data,
                duration,
                media_count,
                total_media,
                submitted_by,
                submission_time,
            ]
            # execute SQL query using execute() method.
            cursor.execute(insert_sql, insert_values)
            connection.commit()


if __name__ == "__main__":
    connection = Connection.get_instance()

    load_table(connection)
    with open("data/data.json", "r") as json_file:
        data = json.load(json_file)

    load_data(connection, data)
