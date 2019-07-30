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
```

### Using docker compose
`docker-compose build`


### Running
Add excel file to data folder and rename it to test.xlsx
then run:
`python importer.py`
