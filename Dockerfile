FROM  python:3.11

WORKDIR /api2

COPY /api2 /api2

RUN pip install -r requirement.txt

CMD [ "python" ,"manage.py" , "runserver"]

EXPOSE 5000