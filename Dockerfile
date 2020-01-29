FROM python:3.7
RUN pip install pipenv
RUN apt update
RUN apt install -y mysql-client
ADD . /code
WORKDIR /code
RUN pipenv install
RUN chmod a+x wait-for-it.sh
CMD ["./wait-for-it.sh", "mysql:3306", "--", "pipenv", "run", "python", "importer.py"]