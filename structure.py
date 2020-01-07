import json

from connection import Connection

FORM_META_DATA = dict()


def process_form(form, group="", table=""):
    field_type = form.get("type", "")
    group = "{}/{}".format(group, form.get("name")) if group else form.get("name")
    choices = ""

    # Create table for repeat and survey objects
    if field_type in ["repeat", "survey"]:
        if field_type == "survey":
            table = form.get("id_string")
            default_form_columns(form, table)
        else:
            table = form.get("name") if len(group) > 64 else group
            FORM_META_DATA[table] = []

    if field_type == "survey":
        group = ""

    if field_type not in ["start", "end", "note", "today", "group", "repeat", "survey"]:
        if field_type in ["select all that apply", "select one"]:
            choices = [c.get("name") for c in form.get("children")]

        field_name = form.get("name") if len(group) > 64 else group

        FORM_META_DATA.get(table).append(
            dict(field_name=field_name, field_type=field_type, field_choices=choices)
        )

    children = form.get("children")
    if children and field_type not in ["select all that apply", "select one"]:
        for child in children:
            process_form(child, group=group, table=table)


def default_form_columns(form, table):
    table = form.get("id_string")
    FORM_META_DATA[table] = []
    FORM_META_DATA.get(table).append(dict(field_name="_id", field_type="integer", field_choices=[]))
    FORM_META_DATA.get(table).append(
        dict(field_name="_submission_time", field_type="text", field_choices=[])
    )


def column_sanitizer(column):
    groups = column.split("/")


def generate_db_structure(connection):

    for table_name in FORM_META_DATA:
        print(table_name)
        columns = ", ".join(
            [
                "`{}` {}".format(meta_data["field_name"], get_mysql_type(meta_data["field_type"]))
                for meta_data in FORM_META_DATA[table_name]
            ]
        )

        create_table_sql = "CREATE TABLE `{}` ({});".format(table_name, columns)
        run_sql(connection, create_table_sql)


def run_sql(connection, sql):
    with connection.cursor() as cursor:
        # execute SQL query using execute() method.
        cursor.execute(sql)
        connection.commit()


def get_mysql_type(field_type):
    if field_type == "integer":
        return "INT"
    elif field_type == "decimal":
        return "DECIMAL"
    elif field_type == "date":
        return "DATE"
    else:
        return "VARCHAR(255)"


if __name__ == "__main__":
    with open("data/forms.json", "r") as json_file:
        form = json.load(json_file)

    process_form(form)
    connection = Connection.get_instance()
    generate_db_structure(connection)

    # print(FORM_META_DATA["/Feedgap_datacollection_forms_Tanzani...ling_v2"])

