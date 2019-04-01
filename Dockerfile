FROM python:3.7
RUN pip install pipenv
ADD . /code
WORKDIR /code
RUN pipenv install
RUN chmod a+x wait-for-it.sh
CMD ["./wait-for-it.sh", "mariadb:3306", "--", "pipenv", "run", "python", "importer.py"]