import json
import os
import requests

from requests.exceptions import HTTPError
from connection import Connection

ONA_API_KEY = os.getenv("ONA_API_KEY")


def run_sql(connection, sql):
    with connection.cursor() as cursor:
        # execute SQL query using execute() method.
        cursor.execute(sql)
        connection.commit()


def check_table_if_exists(connection, table_name):
    with connection.cursor() as cursor:

        # execute SQL query using execute() method.
        cursor.execute(f"SELECT count(id) as total FROM {table_name}")
        connection.commit()

        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print(f"Records in {table_name} : {data} ")

        return data


def load_table(connection, table_name):
    sql_txt = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            xform_data_id INT NOT NULL,
            xform_id INT NOT NULL,
            data JSON NOT NULL,
            edited VARCHAR(255),
            status VARCHAR(255),
            version VARCHAR(255),
            duration DECIMAL,
            media_count INT,
            total_media INT,
            submitted_by VARCHAR(255),
            submission_time DATETIME
        );
    """
    run_sql(connection, sql_txt)


def api_headers():
    return {"Authorization": "Token {}".format(ONA_API_KEY), "Content-Type": "application/json"}


def make_request(url):

    try:
        response = requests.get(url, headers=api_headers())

        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success! Data fetched from the API")
        return response.json()


def load_data(connection, data, table_name):
    insert_sql = f"""
            insert into {table_name} (
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

            insert_values = [
                d["_id"],
                d["_xform_id"],
                d["_edited"],
                d["_status"],
                d["_version"],
                json.dumps(d),
                d["_duration"],
                d["_media_count"],
                d["_total_media"],
                d["_submitted_by"],
                d["_submission_time"],
            ]
            # execute SQL query using execute() method.
            cursor.execute(insert_sql, insert_values)
            connection.commit()
        print("Success! Data saved in the database")


if __name__ == "__main__":
    connection = Connection.get_instance()
    form_id = 438735

    try:
        data = make_request(f"https://api.ona.io/api/v1/forms/{form_id}")
        if data:
            table_name = data["id_string"]
            load_table(connection, table_name)

            last_record = check_table_if_exists(connection, table_name)
            start = last_record.get("total")

            data = make_request(f"https://api.ona.io/api/v1/data/{form_id}?start={start}")

            if data:
                load_data(connection, data, table_name)
    except Exception as e:
        print(f"Something went wrong! {e}")
    finally:
        connection.close()
