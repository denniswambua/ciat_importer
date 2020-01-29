# ciat_importer

## Setup
Install pipenv
For more informantion and installation info -> https://pipenv.readthedocs.io/en/latest/

### Creating virtualenv
```
    pipenv --python 3.7
```

### Activating the virtualenv
```
    pipenv shell
```
### Installing all packages
```
    pipenv install
```

### .env File
Add `.env` file and add the following content
```
DATABASE=mariadb
USERNAME=root
PASSWORD=test
DB_NAME=test
ONA_API_KEY=<Your ona api key>
```

### Running
The script will create the table using the form id_string as the table name.
`python data_importer.py --form <XformID from ona>`


### Querying the database
The main data from ona is stored in data column.
For detailed instruction check mysql documentation

Example:
`select data->"$._id" from <Table name>`

Example querying repeat field
`select data->'$."sect0/sect2/cattle"' from <Table name>`

